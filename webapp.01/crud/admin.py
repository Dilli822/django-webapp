from crud.models import UserInfo
from django.contrib import admin

# Register your models here.

from .models import UserInfo

admin.site.register(UserInfo)
