from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=100)
    institution=models.CharField(max_length=200)
    role=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField(max_length=10)
    def __str__(self):
        return f"Enquiry by {self.name}"