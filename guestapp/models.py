from django.db import models

# Create your models here.
class userTable(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    cpassword = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)

class loginTable(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.username)