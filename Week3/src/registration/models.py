from django.db import models

class register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emailID = models.EmailField(max_length=50)
    password = models.CharField(max_length=15)
    confirm_password = models.CharField(max_length=15)
