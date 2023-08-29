from django import forms
from .models import LoanProposal

class LoanProposalAdminForm(forms.ModelForm):
    class Meta:
        model = LoanProposal
        fields = '__all__'

    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Denied', 'Denied'),
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES)
