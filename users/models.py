# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# hace que la funcion de abajo se ejecute cuando se guarde (post_save) un usuario (settings.AUTH_USER_MODEL)
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:  # solo cuando el usuario ha sido creado (no en las actualizaciones)
        Token.objects.create(user=instance)  # creamos un token