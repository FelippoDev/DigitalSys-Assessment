from django.contrib import admin
from .models import ProposalFieldConfiguration, LoanProposal
from .forms import LoanProposalAdminForm

@admin.register(ProposalFieldConfiguration)
class ProposalFieldConfigurationAdmin(admin.ModelAdmin):
    list_display = ('field_name', 'is_required')


@admin.register(LoanProposal)
class LoanProposalAdmin(admin.ModelAdmin):
    form = LoanProposalAdminForm
    list_display = ('id', 'proposal_amount', 'fullname', 'email', 
        'document_number', 'phone_number', 'status'
    )
    list_filter = ('status',)  # Allow to filter the proposals by status
    search_fields = ('fullname', 'email', 'document_number', 'phone_number')
    
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status == 'Manual Validation':
            return ()
        
        return ('status',)
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['fullname', 'email', 'phone_number']:
            config = ProposalFieldConfiguration.objects.get(
                    field_name=db_field.name
                )
            if config.is_required:
                kwargs['required'] = True
            
        return super().formfield_for_dbfield(db_field, **kwargs)
