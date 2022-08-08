import imp
from django.db import models
from django.db.models.deletion import CASCADE
from dotenv import load_dotenv
import os
from twilio.rest import Client

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=30)
    admin = models.CharField(max_length=30)
    desc = models.CharField(max_length=500)
    poster_link = models.URLField(max_length=200)
    admin_email = models.EmailField(max_length=254)
    

opt = (
    ("President", "President"),
    ("Vice President", "Vice President"),
    ("Member", "Member"),
)

class ClubMembers(models.Model):
    name = models.CharField(max_length=30)
    club_name = models.ForeignKey(Club, on_delete=models.CASCADE)
    position = models.CharField(max_length = 20,choices = opt)
    contact_no = models.BigIntegerField()

class Event(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    poster_link = models.URLField( max_length=200)
    from_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    to_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    host_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=32, default="")

class Participant(models.Model):
    participant_name = models.CharField(max_length=30,default="")
    contact_no = models.BigIntegerField()    
    participant_email = models.EmailField(max_length=254)
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_type = models.CharField(max_length=20)
    no_of_people = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body='Hello There, You have successfully registered in the event.',
            from_=os.environ['MY_NUM1'],
            to=os.environ['MY_NUM2']
            # to = '+918128431262'        
        )

        return super().save(*args, **kwargs)
