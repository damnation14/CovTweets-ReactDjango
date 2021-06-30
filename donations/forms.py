from django import forms
from .models import donations


class DonationForm(forms.ModelForm):

    class Meta:
        model = donations
        fields = ['title', 'description', 'Account_no', 'Phone_number']

    #your_name = forms.CharField(label='Your name', max_length=100)
