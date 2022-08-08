from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from EventManager.models import Event, Participant, Club, ClubMembers
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
# Create your views here.
def index(request):
    return render(request, 'index.html')    

def club_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        admin = request.POST.get('admin')
        desc = request.POST.get('desc')
        poster_link = request.POST.get('poster_link')
        admin_email = request.POST.get('admin_email')

        club = Club(name=name, admin=admin, desc=desc, poster_link=poster_link, admin_email=admin_email)
        club.save()
    return render(request, 'clubreg_form.html')

def club_member_registration(request):
    if request.method == 'POST':
        if(request.POST.get('master_password') == "admin"):
            name = request.POST.get('name')
            club_name = request.POST.get('club_name')
            position = request.POST.get('position')
            contact_no = request.POST.get('contact_no');
            club = Club.objects.all().filter(name=club_name).first()
            
            print(position)
            context = {'club_list': Club.objects.all()}
            memebr = ClubMembers(name=name, club_name = club, position=position, contact_no=contact_no)
            memebr.save()
            return render(request, 'club_members.html', context)

    context = {'club_list': Club.objects.all()}
    print(Club.objects.all())
    return render(request, 'club_members.html', context)
        


def event_registration(request):
    if request.method == 'POST':        
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        poster_link = request.POST.get('poster_link')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        deadline = request.POST.get('deadline')
        host_email = request.POST.get('host_email')
        password = request.POST.get('password')

        if(Event.objects.all().filter(name=name).exists()):
            context = {'messages': "The event with the same name already exists ! Please try other name ."}
            return render(request, 'event_form.html', context)
        if(from_date > to_date or deadline > from_date):
            context = {'messages': "Starting time or End time of the event or Deadline might be wrong ! Please check again ."}
            return render(request, 'event_form.html', context)

        event = Event(name=name, desc=desc, poster_link=poster_link, from_date=from_date, to_date=to_date, deadline=deadline, host_email=host_email, password=password)        

        event.save()
        evt_id = Event.objects.get(name=name).id        
        send_mail(
           'Your event : '+ str(name),
            'Here is the confirmation message.\n Good Luck ! Your event id is ' + str(evt_id),
            os.environ.get("EMAIL_HOST_USER"),
            [host_email],
            fail_silently=False,
        )        
        context = {'success': "Your event confirmation message has been sent to your registered email ID!"}
        return render(request, 'event_form.html', context)
    return render(request, 'event_form.html')

def participant_registration(request):
    if request.method == 'POST':
        participant_name = request.POST.get('participant_name')
        contact_no = request.POST.get('contact_no')
        participant_email = request.POST.get('participant_email')
        event_name = request.POST.get('event_name')
        registration_type = request.POST.get('registration_type')
        no_of_people = request.POST.get('no_of_people')    
        evnt = Event.objects.all().filter(name=event_name).first()   

        # Already Registered
        if Participant.objects.all().filter(participant_name=participant_name, contact_no=contact_no,participant_email=participant_email,event_name=evnt):
            context = {'event_list': Event.objects.all().filter(deadline__gte=datetime.now()) ,'messages':"You have already participated in the event !"}
            return render(request, 'participation_form.html', context)

        # New participant
        participant = Participant(participant_name=participant_name, contact_no=contact_no, participant_email=participant_email, event_name=evnt, registration_type=registration_type, no_of_people=no_of_people)

        participant.save()
        context = {'success': "Your participation is successfully registered !",
                   'event_list': Event.objects.all().filter(deadline__gte=datetime.now())}
        return render(request, 'participation_form.html', context)
        # print(participant)        

    context = {'event_list': Event.objects.all().filter(deadline__gte=datetime.now())}
    return render(request, 'participation_form.html', context)

def event_dashboard(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        password = request.POST.get('password')

        
        if  Event.objects.all().filter(id=event_id).exists() and Event.objects.get(id=event_id).password == password:
            context = {'participant_list': Participant.objects.all().filter(event_name=event_id)}
            return render(request, 'event_dashboard.html',context) 
        else:
            context = {'messages':"Username or password is incorrect !"}
            return render(request, 'event_dashboard.html', context)
    return render(request, 'event_dashboard.html')

