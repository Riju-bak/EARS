from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomUserAddForm


class SignupView(CreateView):
    form_class = CustomUserAddForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
