from django.contrib import admin
from .models import Client , Projects, Project_Users
# Register your models here.


admin.site.register(Client)
admin.site.register(Projects)
admin.site.register(Project_Users)
