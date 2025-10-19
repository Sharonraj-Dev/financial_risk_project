"""
Defines the views for the risk_app, handling user input and
displaying prediction results.
"""
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import PredictionForm
from .utils import predict_from_dict
from .models import Applicant


def home(request):
    result = None
    if request.method == "POST":
        income = float(request.POST.get("income").replace(",", "").strip())
        loan = float(request.POST.get("loan_amount").replace(",", "").strip())
        credit = float(request.POST.get("credit_score").replace(",", "").strip())


        # Simple dummy risk logic for now:
        if credit < 600 or loan > income * 0.5:
            result = "High Risk ⚠️"
        elif 600 <= credit < 750:
            result = "Medium Risk ⚠"
        else:
            result = "Low Risk ✅"

    return render(request, "risk_app/home.html", {"result": result})


"""def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello! This is the Financial Risk Prediction App.")
    # If the form is submitted (POST request)
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = PredictionForm(request.POST)
        
        # Check if the form data is valid
        if form.is_valid():
            # Process the data in form.cleaned_data
            data = form.cleaned_data
            
            # Get prediction and probability from the ML model utility
            prediction, probability = predict_from_dict(data)
            
            # Create a new Applicant record in the database with the form data
            # and the prediction result.
            applicant = Applicant.objects.create(
                **data, 
                predicted_risk=prediction
            )
            
            # Render the results page with the prediction context
            context = {
                'prediction': prediction,
                'probability': probability,
                'applicant': applicant,
            }
            return render(request, 'risk_app/predict_result.html', context)
            
    # If it's a GET request (or any other method), create a blank form
    else:
        form = PredictionForm()

    # Render the main page with the form
    return render(request, 'risk_app/home.html', {'form': form})"""