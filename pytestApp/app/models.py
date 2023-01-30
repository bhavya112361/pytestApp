from django.db import models
from django.utils import timezone
from django.conf import settings
import uuid

# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at=models.DateField(auto_now_add=True)

#     class Meta:
#         abstract=True


class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name
    
    
class Projects(models.Model):
    project_name = models.CharField(max_length=255)
    client_id=models.ForeignKey(Client,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING )
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.project_name
    
class Project_Users(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE )
    User_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.project_id)

