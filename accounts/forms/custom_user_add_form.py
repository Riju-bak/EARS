from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


# To let an admin add a new user
class CustomUserAddForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "type")
