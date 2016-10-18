from django.contrib.auth.models import User
from django.test import override_settings
from rest_framework.test import APITestCase
from rest_framework import status

from followers.models import Relationship


@override_settings(ROOT_URLCONF='followers.urls')
class FollowAPITests(APITestCase):

    FOLLOW_API_URL = '/follow/'
    USERS_PASSWORD = "starwars"

    def setUp(self):
        self.user1 = User.objects.create_user('luke', "skywalker@starwars.com", self.USERS_PASSWORD)

    def test_endpoint_returns_403_when_user_is_not_authenticated(self):
        response = self.client.post(self.FOLLOW_API_URL, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_endpoint_returns_400_bad_request_when_no_target_user_is_sent(self):
        self.client.login(username=self.user1.username, password=self.USERS_PASSWORD)
        response = self.client.post(self.FOLLOW_API_URL, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('target', response.data)
        self.assertEqual(response.data.get('target'), ["This field is required."])

    def test_endpoint_returns_400_bad_request_when_target_user_doesnt_exist(self):
        self.client.login(username=self.user1.username, password=self.USERS_PASSWORD)
        response = self.client.post(self.FOLLOW_API_URL, {'target': 0})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('target', response.data)
        self.assertEqual(response.data.get('target'), ['Invalid pk "0" - object does not exist.'])

    def test_endpoint_returns_400_bad_request_when_target_user_is_already_followed(self):
        user2 = User.objects.create_user('anakin', "anakin@starwars.com", self.USERS_PASSWORD)
        Relationship.objects.create(origin=self.user1, target=user2)
        response = self.client.post(self.FOLLOW_API_URL, {'target': user2.pk})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
