from django.db import models




class Applicant(models.Model):
    income = models.FloatField()
    age = models.IntegerField()
    credit_score = models.FloatField()
    debt = models.FloatField()
    employment_status = models.CharField(max_length=100)
    
    loan_amount = models.FloatField()
    loan_term_months = models.IntegerField()
    credit_score = models.FloatField()
    num_of_defaults = models.IntegerField()
    employment_years = models.FloatField()
    predicted_risk = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Risk Data ({self.income}, {self.credit_score})"