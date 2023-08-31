from django.db import models

class LoanProposal(models.Model):
    proposal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    fullname = models.CharField(max_length=180, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    document_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    
    def __str__(self):
        return f"Proposal {self.id}"
    
    
class ProposalFieldConfiguration(models.Model):
    field_name = models.CharField(max_length=255)
    is_required = models.BooleanField(default=False)

