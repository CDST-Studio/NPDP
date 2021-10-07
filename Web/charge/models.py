from django.db import models

class Post(models.Model):
    content = models.TextField(blank = True)

    image = models.ImageField(upload_to = 'Orders/',blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

