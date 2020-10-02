from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=254)
    description = models.TextField(max_length=122)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
    