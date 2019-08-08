from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .models import User


# from https://dyve.net/post/django-custom-user-model-admin/
class UserAdminWithExtraFields(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdminWithExtraFields, self).__init__(*args, **kwargs)

        abstract_fields = [field.name for field in AbstractUser._meta.fields]
        user_fields = [field.name for field in self.model._meta.fields]

        self.fieldsets += (
            (
                _('Extra fields'),
                {
                    'fields': [
                        f
                        for f in user_fields
                        if (f not in abstract_fields and f != self.model._meta.pk.name)
                    ]
                },
            ),
        )


admin.site.register(User, UserAdminWithExtraFields)
