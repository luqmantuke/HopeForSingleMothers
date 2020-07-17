from django.forms import ModelForm
from HFSM.models import Contact
from django.core.exceptions import ValidationError

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
  

