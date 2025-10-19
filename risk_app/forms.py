"""
Defines the form used to accept input for risk prediction.
"""
from django import forms


class PredictionForm(forms.Form):
    """
    A Django form for validating financial risk prediction inputs.
    
    Matches the features expected by the trained model.
    """
    income = forms.FloatField(
        min_value=0,
        label="Annual Income",
        help_text="Enter your total annual income.",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    age = forms.IntegerField(
        min_value=18,
        label="Age",
        help_text="Enter your current age (must be 18 or older).",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    loan_amount = forms.FloatField(
        min_value=0,
        label="Loan Amount",
        help_text="Enter the total amount of the loan you are requesting.",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    loan_term_months = forms.IntegerField(
        min_value=1,
        label="Loan Term (Months)",
        help_text="Enter the desired loan term in months.",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    credit_score = forms.FloatField(
        min_value=300,
        max_value=850,
        label="Credit Score",
        help_text="Enter your current credit score (e.g., 300-850).",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    num_of_defaults = forms.IntegerField(
        min_value=0,
        label="Number of Past Defaults",
        help_text="Enter the total number of times you have defaulted on a loan.",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    employment_years = forms.FloatField(
        min_value=0,
        label="Years of Employment",
        help_text="Enter the number of years at your current job.",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
    )