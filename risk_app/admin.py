from django.contrib import admin
from .models import Applicant

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('id', 'income', 'loan_amount', 'credit_score', 'predicted_risk', 'created_at')
    list_filter = ('predicted_risk',)
    search_fields = ('id',)
