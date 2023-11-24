from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserAddForm, CustomUserEditForm
from accounts.models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserAddForm
    form = CustomUserEditForm
    model = CustomUser
    list_display = ["email", "username", "type", "is_staff"]
    fieldsets = UserAdmin.fieldsets + \
                (
                    (None, {
                        'fields': [
                            'type',
                        ],
                    }
                     ),
                )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ["type", ]}),)


admin.site.register(CustomUser, CustomUserAdmin)
