from django.db import models

# Create your models here.
class userTable(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    cpassword = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)

class loginTable(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.username)