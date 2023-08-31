from celery import shared_task
from digitalsys.services.loan_api.external_api import LoanApiVerifier
from digitalsys.loan.models import LoanProposal

@shared_task
def credit_analysis_background_task(document, fullname):
    verifier = LoanApiVerifier()
    status = verifier.loan_analysis(document=document, fullname=fullname)
    loan = LoanProposal.objects.filter(
            document_number=document
        ).first()
    if status:
        loan.status = "Manual Validation"
        loan.save()
    else:
        loan.status = "Denied"
        loan.save()
