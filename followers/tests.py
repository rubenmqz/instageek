from django.contrib.auth.models import User
from django.test import TestCase

from followers.models import Relationship


class RelationshipTests(TestCase):

    def test_relationship_related_names_work_properly(self):

        user1 = User.objects.create_user("luke", "skywalker@starwars.com", "skywalker")
        user2 = User.objects.create_user("anakin", "annie@starwars.com", "skywalker")

        Relationship.objects.create(origin=user1, target=user2)

        self.assertEqual(user2, user1.following.all()[0]) #el único usuario al que sigue el user1 es el user 2
