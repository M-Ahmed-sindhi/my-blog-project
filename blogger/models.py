from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    picture = models.ImageField(upload_to='blog_images/', blank=True, null=True) 

    def __str__(self):
        return self.title + ' | ' + str(self.author)

# Create your models here.
