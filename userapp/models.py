from django.db import models
from bookapp.models import Book
from guestapp.models import userTable
# Create your models here.

class Cart(models.Model):
          id = models.AutoField(primary_key=True)
          user = models.OneToOneField(userTable,on_delete=models.CASCADE)
          item = models.ManyToManyField(Book)
          
class CartItem(models.Model):
          cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
          book = models.ForeignKey(Book,on_delete=models.CASCADE)
          quantity = models.PositiveIntegerField(default=1)