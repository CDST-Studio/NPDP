from django.db import models

class Post(models.Model):
    user_name = models.CharField(max_length = 30,blank = True)
    content = models.TextField(blank = True)

    image = models.ImageField(upload_to = 'Orders/',blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'[{self.pk}] {self.user_name}'