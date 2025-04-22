from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=252)
    thumbnailUrl = models.CharField(max_length=252)
    pagecount = models.IntegerField(default=0)  
    shortDescription = models.CharField(null=True)
    longDescription = models.TextField(null=True)
    auther = models.CharField(null=True, max_length=252)
    image = models.ImageField(upload_to='images', null=True)
    
    
    def __str__(self):
        return f'{self.title} - {self.pagecount}'

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_txt = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return f'{self.review_txt[:5]} - {self.created_date}'
