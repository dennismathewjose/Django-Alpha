#a signal which gets fired when an object is saved

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import Profile

#User -> sender who sends the signal
#receiver -> who receives the message send by User

@receiver(post_save, sender = User) 
def CreateProfile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user = instance)
#when a user is saved, then send this signal
#then this signal is received by a receiver. receiver : CreateProfile function 
#the function takes all the arguments send by the sender

@receiver(post_save, sender = User) 
def SaveProfile(sender, instance, **kwargs):  
    instance.profile.save()