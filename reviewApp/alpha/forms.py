from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    subject = forms.CharField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)



