from django import forms
from .models import PurchaseInquiry
from .models import ContactMessage

class PurchaseInquiryForm(forms.ModelForm):
    class Meta:
        model = PurchaseInquiry
        fields = ['product', 'price', 'name', 'email', 'address','message']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
