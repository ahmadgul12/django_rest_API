

from django.db import models

# Create your models here.

class product(models.Model):
    title=models.TextField()
    Description=models.TextField()
    price=models.TextField()

    def __str__(self):
        return self.title