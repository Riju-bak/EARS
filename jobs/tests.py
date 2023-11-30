from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import CustomUser
from jobs.models import Job


# Create your tests here.
class JobTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.dummyuser = CustomUser.objects.create_user("somefac", "somefac@gmail.com", "randompasswd",
                                                       type=CustomUser.Type.FACULTY)
        cls.profile_url = f"/accounts/{cls.dummyuser.pk}/profile/"

        cls.dummyJobOne = Job.objects.create(title="Gaming Lab Assistant",
                                             description="Need a lab assistant with experience in Unity")
        cls.dummyJobTwo = Job.objects.create(title="Gaming Lab Assistant",
                                             description="Need a lab assistant with experience in Unity")

    def test_joblist_page_exists(self):
        logged_in = self.client.login(username="somefac", password="randompasswd")
        self.assertTrue(logged_in)
        res = self.client.get("/jobs/")
        self.assertEqual(res.status_code, 200)

    def test_job_detail_page(self):
        logged_in = self.client.login(username="somefac", password="randompasswd")
        self.assertTrue(logged_in)
        res = self.client.get(f"/jobs/{self.dummyJobOne.pk}/")
        self.assertEqual(res.status_code, 200)

    def test_jobcreate(self):
        pass
