from django.db import models

class PurchaseInquiry(models.Model):
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address=models.CharField(max_length=100)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    

