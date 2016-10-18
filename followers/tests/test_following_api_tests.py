from django.contrib.auth.models import User
from django.test import override_settings
from rest_framework import status
from rest_framework.test import APITestCase

from followers.models import Relationship


@override_settings(ROOT_URLCONF='followers.urls')
class FollowingAPITests(APITestCase):

    FOLLOWING_API_URL = '/following/'
    USERS_PASSWORD = 'skywalker'

    def setUp(self):
        self.user1 = User.objects.create_user("luke", "skywalker@starwars.com", self.USERS_PASSWORD)
        self.user2 = User.objects.create_user("anakin", "annie@starwars.com", self.USERS_PASSWORD)
        self.user3 = User.objects.create_user("chewie", "chewie@starwars.com", self.USERS_PASSWORD)
        self.user4 = User.objects.create_user("han", "han@starwars.com", self.USERS_PASSWORD)
        self.user5 = User.objects.create_user("r2d2", "r2d2@starwars.com", self.USERS_PASSWORD)
        self.user6 = User.objects.create_user("c3po", "c3po@starwars.com", self.USERS_PASSWORD)
        self.user7 = User.objects.create_user("leia", "leia@starwars.com", self.USERS_PASSWORD)
        self.user8 = User.objects.create_user("finn", "finn@starwars.com", self.USERS_PASSWORD)

        #crear relaciones del user1
        Relationship.objects.create(origin=self.user1, target=self.user2)
        Relationship.objects.create(origin=self.user1, target=self.user3)
        Relationship.objects.create(origin=self.user1, target=self.user4)
        Relationship.objects.create(origin=self.user1, target=self.user5)
        Relationship.objects.create(origin=self.user1, target=self.user6)
        Relationship.objects.create(origin=self.user1, target=self.user7)
        Relationship.objects.create(origin=self.user1, target=self.user8)

        # crear relaciones del user3
        # Relationship.objects.create(origin=self.user1, target=self.user2)
        Relationship.objects.create(origin=self.user3, target=self.user1)
        Relationship.objects.create(origin=self.user3, target=self.user2)
        Relationship.objects.create(origin=self.user3, target=self.user4)

    def test_following_users_endpoint_fails_when_user_is_not_authenticated(self):

        Relationship.objects.create(origin=self.user1, target=self.user2)  # user1 sigue a user2

        # hacer peticion
        response = self.client.get(self.FOLLOWING_API_URL)

        # asegurar que la respuesta es un codigo 403
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_doesnt_follow_any_user_and_empty_list_is_returned(self):

        # autenticar al user2
        self.client.login(username=self.user2.username, password=self.USERS_PASSWORD)

        # hacer peticion
        response = self.client.get(self.FOLLOWING_API_URL)

        # asegurar que la respuesta es un codigo 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # asegurar que la longitud de los datos devueltos es 0
        self.assertEqual(len(response.data), 0)

    def test_user_follows_three_users_and_three_users_are_returned(self):

        # autenticar al user3
        self.client.login(username=self.user3.username, password=self.USERS_PASSWORD)

        # hacer peticion
        response = self.client.get(self.FOLLOWING_API_URL)

        # asegurar que la respuesta es un codigo 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # asegurar que la longitud de los datos devueltos es 3
        self.assertEqual(len(response.data), 3)

    def test_user_follows_seven_users_and_seven_users_are_returned(self):

        # autenticar al user1
        self.client.login(username=self.user1.username, password=self.USERS_PASSWORD)

        # hacer peticion
        response = self.client.get(self.FOLLOWING_API_URL)

        # asegurar que la respuesta es un codigo 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # asegurar que la longitud de los datos devueltos es 7
        self.assertEqual(len(response.data), 7)
