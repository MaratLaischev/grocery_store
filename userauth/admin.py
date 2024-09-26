from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy

from userauth.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'is_staff',
        'date_joined',
        'last_login'
    )

    search_fields = ('id', 'username')
    list_filter = ('is_staff',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
