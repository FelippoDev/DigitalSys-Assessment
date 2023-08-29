from rest_framework import serializers
from .models import LoanProposal, ProposalFieldConfiguration

class LoanProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProposal
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        proposal_fields = (
            ProposalFieldConfiguration.objects.filter(is_displayed=True)
        )
        for field in proposal_fields:
            self.fields[field.field_name].required = field.is_required


