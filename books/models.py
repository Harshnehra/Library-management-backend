from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    bookImage = models.CharField(max_length=500,blank=True, null=True)
    published_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
