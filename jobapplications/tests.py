from django.test import TestCase

from accounts.models import CustomUser
from jobapplications.models import JobApplication, Comment
from jobs.models import Job


# Create your tests here.
class JobApplicationsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.dummyuser = CustomUser.objects.create_user("somefac", "somefac@gmail.com", "randompasswd",
                                                       type=CustomUser.Type.APPLICANT)
        cls.profile_url = f"/accounts/{cls.dummyuser.pk}/profile/"
        cls.dummyJobOne = Job.objects.create(title="Gaming Lab Assistant",
                                             description="Need a lab assistant with experience in Unity")
        cls.dummyJobTwo = Job.objects.create(title="Mobile App Lab Assistant",
                                             description="Need a lab assistant with experience in React-native and Android App Dev")

        cls.dummyJobApplicationOne = JobApplication.objects.create(job=cls.dummyJobOne,
                                                                   body="Something about the applicant, relevant to Gaming Lab Assitant position",
                                                                   author=cls.dummyuser)

    def test_listusersjobapplications(self):
        logged_in = self.client.login(username="somefac", password="randompasswd")
        res = self.client.get(f"/applications/?author={self.dummyuser.pk}")
        self.assertEqual(res.status_code, 200)

    def test_jobapplicationdetail(self):
        logged_in = self.client.login(username="somefac", password="randompasswd")
        res = self.client.get(f"/applications/{self.dummyJobApplicationOne.pk}/")
        self.assertEqual(res.status_code, 200)

    def test_jobapplicationcreate(self):
        logged_in = self.client.login(username="somefac", password="randompasswd")
        res = self.client.post(f"/applications/new/",
                               {
                                   "job": self.dummyJobTwo.pk,
                                   "body": "Something about the applicant, relevant to Mobile App Lab Assistant position",
                               })
        self.assertEqual(res.status_code, 302)
        self.assertEqual(JobApplication.objects.all().count(), 2)
        newly_create_jobapp = JobApplication.objects.all()[1]
        self.assertEqual(newly_create_jobapp.body,
                         "Something about the applicant, relevant to Mobile App Lab Assistant position")

    def test_jobapplicationupdate(self):
        logged_in = self.client.login(username="somefac", password="randompasswd")
        res = self.client.post(f"/applications/{self.dummyJobApplicationOne.pk}/edit/",
                               {
                                   "body": "Update application body",
                               })
        self.assertEqual(res.status_code, 302)
        jobapp = JobApplication.objects.get(pk=self.dummyJobApplicationOne.pk)
        self.assertEqual(jobapp.body, "Update application body")

    def test_jobapplicationdelete(self):
        logged_in = self.client.login(username="somefac", password="randompasswd")
        res = self.client.post(f"/applications/{self.dummyJobApplicationOne.pk}/delete/")
        self.assertEqual(JobApplication.objects.all().count(), 0)

    def test_writecomment(self):
        logged_in = self.client.login(username="somefac", password="randompasswd")
        res = self.client.post(f"/applications/{self.dummyJobApplicationOne.pk}/",
                               {
                                   "comment": "this is a test comment",
                               })
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Comment.objects.filter(jobapplication=self.dummyJobApplicationOne).count(), 1)