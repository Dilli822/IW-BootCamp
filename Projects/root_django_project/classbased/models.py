# from django.db import models

# # Create your models here.

# class ClassBasedModel(models.Model):
#     name = models.CharField(max_length=100)


# making crud samemodels for templates
# as templates were copied from crud 
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name =models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    bio = models.TextField()


    # string represention overridding
    def __str__(self):
        return self.email

