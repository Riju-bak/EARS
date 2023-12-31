from django.urls import path
from django.views.generic import TemplateView

from .views import SignupView, UserProfileView

urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    path('<int:pk>/profile/', UserProfileView.as_view(), name="profile"),
    path('editprofilesuccess/', TemplateView.as_view(template_name="registration/edituserprofilesuccess.html"),
         name="editprofilesuccess"),
]
