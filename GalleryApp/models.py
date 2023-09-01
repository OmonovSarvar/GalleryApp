from django.db import models
from django.utils import timezone
from django.contrib.auth.admin import User


# Create your models here.

class Info(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=33)
    author = models.CharField(max_length=55)
    img_date = models.DateField(default=timezone.datetime.now)

    def __str__(self):
        return f"{self.img_date}da {self.author} tomonidan rasm joylandi"
