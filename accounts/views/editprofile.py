from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from ..forms import CustomUserEditForm
from ..models import CustomUser


# class EditUserProfileView(UpdateView):
#     form_class = CustomUserEditForm
#     template_name = "registration/edituserprofile.html"
#     success_url = reverse_lazy("home")

class EditUserProfileView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserEditForm
    success_message = "Profile updated successfully"
    template_name = "registration/edituserprofile.html"
    success_url = reverse_lazy("editprofilesuccess")

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk

    def form_valid(self, form):
        password = form.cleaned_data.get('password')
        if password:
            self.object.set_password(password)
            self.object.save()

            # Logout the user
            logout(self.request)

        return super().form_valid(form)