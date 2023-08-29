from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import LoanProposalSerializer, \
    ProposalFieldConfigurationSerializer
from .tasks import credit_analysis_background_task
from .models import ProposalFieldConfiguration

class LoanProposalAPIView(CreateAPIView):
    serializer_class = LoanProposalSerializer
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        credit_analysis_background_task(
            response.data['document_number'], response.data['fullname']
        )
        return response

    
class ProposalFieldConfigurationAPIView(ListAPIView):
    serializer_class = ProposalFieldConfigurationSerializer
    queryset = ProposalFieldConfiguration.objects.all()