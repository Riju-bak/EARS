from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser


class ProfileEditTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.dummyuser = CustomUser.objects.create_user("someuser", "someuser@gmail.com", "randompasswd", type=CustomUser.Type.APPLICANT)
        cls.profile_url = f"/accounts/{cls.dummyuser.pk}/profile/"

    def test_profile_page_exists(self):
        logged_in = self.client.login(username="someuser", password="randompasswd")
        self.assertTrue(logged_in)
        res = self.client.get(self.profile_url)
        self.assertEqual(res.status_code, 200)

    def test_profile_page_rev(self):
        logged_in = self.client.login(username="someuser", password="randompasswd")
        self.assertTrue(logged_in)
        res = self.client.get(reverse("profile", kwargs={'pk': self.dummyuser.pk}))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "registration/profile.html")

    def test_profile_edit(self):
        logged_in = self.client.login(username="someuser", password="randompasswd")
        self.assertTrue(logged_in)
        res = self.client.post(reverse("profile", kwargs={'pk': self.dummyuser.pk}),
                               {
                                   "first_name": "TestUserFirstName",
                                   "last_name": "TULastName",
                                   "email": "testuser@dummy.com",
                                   "password": "abcd",
                                   "confirm_password": "abcd",
                               })
        self.assertEqual(res.status_code, 302)
        self.dummyuser = CustomUser.objects.get(pk=self.dummyuser.pk)
        self.assertEqual(self.dummyuser.last_name, "TULastName")
        logged_in = self.client.login(username="someuser", password="abcd")
        self.assertTrue(logged_in)
