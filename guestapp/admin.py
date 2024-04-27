from django.contrib import admin
from .models import userTable,loginTable
# Register your models here.
admin.site.register(userTable)
admin.site.register(loginTable)