from django.contrib import admin
from .models import Event, Participant, Club, ClubMembers
# Register your models here.

admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Club)
admin.site.register(ClubMembers)
