from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

from accounts.forms import CustomUserAddForm
from accounts.models import CustomUser


# To let an admin make changes to a user
class CustomUserEditForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data
