from django.db import models

# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

#Show entry in admin panel by name
    def __str__(self):
        return self.name
