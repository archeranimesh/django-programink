from django import forms
from .models import HelloCustomer


class HelloCandidateForm(forms.ModelForm):
    class Meta:
        # Model Class Name
        model = HelloCustomer
        # Form will be created for all fields.
        fields = "__all__"
