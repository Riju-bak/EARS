from django.contrib.auth.forms import UserChangeForm

from accounts.forms import CustomUserAddForm
from accounts.models import CustomUser


# To let an admin make changes to a user
class CustomUserEditForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = CustomUserAddForm.Meta.fields
