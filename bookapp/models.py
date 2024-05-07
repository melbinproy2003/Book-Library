from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return '{}'.format(self.name)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='book_media')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{}'.format(self.title)