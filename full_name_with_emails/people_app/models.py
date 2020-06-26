from django.db import models


class People(models.Model):

    First_Name = models.CharField(max_length = 200)
    Last_Name = models.CharField(max_length = 200)
    Email = models.EmailField(max_length = 200, unique = True)
