from django.contrib.auth.models import User
from django.db import models

class Relationship(models.Model):

    origin = models.ForeignKey(User, related_name='follower') #usuario que sigue
    target = models.ForeignKey(User, related_name='following') #usuario al que sigue
    created_at = models.DateTimeField(auto_now_add=True)
