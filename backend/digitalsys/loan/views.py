from rest_framework.generics import CreateAPIView
from .serializers import LoanProposalSerializer
from .tasks import credit_analysis_background_task

class LoanProposalAPIView(CreateAPIView):
    serializer_class = LoanProposalSerializer
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        credit_analysis_background_task(
            response.data['document_number'], response.data['fullname']
        )
        return response

    
