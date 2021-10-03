from django.db import models

class Order(models.Model):
    user_name = models.CharField(max_length = 255, null = True)
    content = models.TextField(max_length = 300)

    
    image = models.ImageField(upload_to = 'Video/') #upload_to는 경로를 지정 여기에 저장하라는 의미이다.

    def __str__(self):
        return f'[{self.pk}]{self.user_name}'