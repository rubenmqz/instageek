from django.contrib.auth.models import User
from rest_framework import serializers

from followers.models import Relationship


class RelationshipUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User


class RelationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relationship
        read_only_fields = ('origin',)

    def validate_target(self, value):
        return value

    def validate(self, attrs):
        return attrs
