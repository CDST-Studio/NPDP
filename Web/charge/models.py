from django.db import models

class Order(models.Model):
    user_name = models.CharField(max_length = 30, null = True)
    content = models.TextField(max_length = 300)

    order_at = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return f'[{self.pk}]{self.user_name}'