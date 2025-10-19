from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import predict_from_dict

@csrf_exempt
def predict_json(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=400)
    try:
        payload = json.loads(request.body)
    except Exception:
        return JsonResponse({'error': 'invalid json'}, status=400)

    required = ['income','age','loan_amount','loan_term_months','credit_score','num_of_defaults','employment_years']
    if not all(k in payload for k in required):
        return JsonResponse({'error': f'missing keys, required: {required}'}, status=400)

    try:
        pred, prob = predict_from_dict(payload)
    except FileNotFoundError as e:
        return JsonResponse({'error': str(e)}, status=500)
    except Exception as e:
        return JsonResponse({'error': 'internal error', 'detail': str(e)}, status=500)

    return JsonResponse({'prediction': pred, 'probability': prob})
