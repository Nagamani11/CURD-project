from django.db import models
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    experience = models.IntegerField()
    skill = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
