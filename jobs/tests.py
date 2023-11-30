from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

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
        cls.dummyJobTwo = Job.objects.create(title="Mobile App Lab Assistant",
                                             description="Need a lab assistant with experience in React-native and Android App Dev")

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
        logged_in = self.client.login(username="somefac", password="randompasswd")
        res = self.client.post(reverse("jobcreate"),
                               {
                                   "title": "randomtitle",
                                   "description": "randomdescription",
                               })
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Job.objects.all().count(), 3)
        newly_created_job = Job.objects.all()[2]
        self.assertEqual(newly_created_job.title, "randomtitle")
        self.assertEqual(newly_created_job.description, "randomdescription")

    def test_jobupdate(self):
        logged_in = self.client.login(username="somefac", password="randompasswd")
        res = self.client.post(f"/jobs/{self.dummyJobOne.pk}/edit/",
                               {
                                   "title": "Game-Lab Assistant",
                                   "description": "Need a lab assistant with experience in Unity",
                               })
        job = Job.objects.get(pk=self.dummyJobOne.pk)
        self.assertEqual(job.title, "Game-Lab Assistant")
        self.assertEqual(job.description, "Need a lab assistant with experience in Unity")

    def test_jobdelete(self):
        logged_in = self.client.login(username="somefac", password="randompasswd")
        res = self.client.post(f"/jobs/{self.dummyJobOne.pk}/delete/")
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Job.objects.count(), 1)
