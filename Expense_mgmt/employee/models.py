from django.db import models
from django.contrib.auth.models import User

class EmployeeExpense(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    category = models.CharField(max_length=100)
    paid_by = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.employee.username} - {self.category} - {self.amount}"
