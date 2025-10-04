from django.db import models
from django.conf import settings

class Expense(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10)
    converted_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    date = models.DateField()
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Expense {self.id} - {self.employee} - {self.amount} {self.currency}"
