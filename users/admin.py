from django.contrib import admin
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin



class CustomerUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "user Type",
            {
                "fields":(
                    "is_teacher",
                    "is_student",
                )
            }
        )
    )
    


admin.site.register(User, CustomerUserAdmin)