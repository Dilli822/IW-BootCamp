from django.db import models

# Create your models here.
# from user.models import User 
from django.contrib.auth import get_user_model

class StatusMessage(models.Model):
    status = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(),null=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user