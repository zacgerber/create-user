from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from myuser.models import MyUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'age',
                    'displayname',
                    'homepage',
                )
            }
        )
    )


admin.site.register(MyUser, CustomUserAdmin)
