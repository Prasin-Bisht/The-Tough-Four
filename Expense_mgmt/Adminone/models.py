from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AccountModel(models.Model):
    STATUS_CHOICES = [
    ('Usa', 'USA'),
    ('India','INDIA'),
    ('Canada', 'CANADA'),
    ]

    ROLE_CHOICES = [
    ('Manager','MANAGER'),
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

class Expense(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')


class ApprovalRule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approval_rules')
    approvers = models.ManyToManyField(User, related_name='approves')
    is_manager_approver = models.BooleanField(default=True)
    min_approval_percentage = models.PositiveIntegerField(default=100)