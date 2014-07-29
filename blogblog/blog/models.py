from django.db import models

# Create your models here.

class Posts(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    writer = models.CharField(max_length=50)
    created_at =  models.DateTimeField(auto_now_add=True)

# tools - run ...task