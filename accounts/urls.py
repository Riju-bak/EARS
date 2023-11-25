from django.urls import path
from django.views.generic import TemplateView

from .views import SignupView, EditUserProfileView

urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    path('<int:pk>/editprofile/', EditUserProfileView.as_view(), name="editprofile"),
    path('editprofilesuccess/', TemplateView.as_view(template_name="registration/edituserprofilesuccess.html"),
         name="editprofilesuccess"),
]
