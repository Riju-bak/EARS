from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class SignupTests(TestCase):
    def test_signup_page_exists(self):
        relative_url = "/accounts/signup/"
        res = self.client.get(relative_url)
        self.assertEqual(res.status_code, 200)

    def test_signup_page_rev(self):
        res = self.client.get(reverse("signup"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "registration/signup.html")

    def test_signup_form(self):
        custom_user_model = get_user_model()
        res = self.client.post(reverse("signup"),
                               {
                                   "username": "someuser",
                                   "email": "someuser@gmail.com",
                                   "first_name": "Some",
                                   "last_name": "User",
                                   "type": custom_user_model.Type.APPLICANT,
                                   "password1": "somepassword123",
                                   "password2": "somepassword123",
                               })
        self.assertEqual(res.status_code, 302)
        self.assertEqual(custom_user_model.objects.all().count(), 1)
        newly_created_user = custom_user_model.objects.all()[0]
        self.assertEqual(newly_created_user.username, "someuser")
        self.assertEqual(newly_created_user.type, custom_user_model.Type.APPLICANT)
