from django.urls import path
from . import views

urlpatterns = [
    path('loan', views.LoanProposalAPIView.as_view()),
    path('proposal-fields', views.ProposalFieldConfigurationAPIView.as_view()),
]
