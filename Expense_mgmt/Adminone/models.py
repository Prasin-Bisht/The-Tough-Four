from django.db import models

# Create your models here.
class AccountModel(models.Model):
    STATUS_CHOICES = [
    ('Usa', 'USA'),
    ('India','INDIA'),
    ('Canada', 'CANADA'),
    ]

    ROLE_CHOICES = [
    ('Manager','MANaGER'),
    ('employee','EMPLOYEE'),

    ]
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField()
    confirmpassword = models.CharField()
    countrySelection = models.CharField(max_length=25,choices=STATUS_CHOICES)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
    manager = models.CharField(max_length=50)

def __str__(self):
        return self.name