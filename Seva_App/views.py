import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render
from NLPTransformer import process_symptoms
from disease_names import DISEASE_NAMES, get_disease_name

# Dynamically set path to your ML model file
MODEL_FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),  # Parent directory
    "LR-83.pkl"
)

# Import get_prediction with fixed path
from predict import get_prediction  


@require_GET
def home(request):
    return render(request, 'home.html')


@require_GET
def get_matches(request):
    user_input = request.GET.get("user_input", "")
    matched_symptoms = process_symptoms(user_input)
    return JsonResponse({"matched_symptoms": matched_symptoms})


# Update the predict function to prevent duplicate categories

@csrf_exempt
@require_POST
def predict(request):
    try:
        body = json.loads(request.body.decode("utf-8"))
        matched_symptoms = body.get("matched_symptoms", [])

        # Get predictions
        predictions = get_prediction(matched_symptoms, MODEL_FILE_PATH)
        
        if predictions is not None:
            # Create a list of results with disease names included
            prediction_results = []
            seen_categories = set()  # Track seen categories to avoid duplicates
            
            # Sort indices by probability (highest first)
            top_indices = sorted(range(len(predictions)), 
                                key=lambda i: predictions[i], 
                                reverse=True)
            
            # Get properly named diseases (no duplicates)
            for i in top_indices:
                disease_name = get_disease_name(i)
                
                # Skip any generic conditions
                if "Medical Condition" in disease_name:
                    continue
                
                # Get category (everything before "Type" if present)
                category = disease_name.split(" Type ")[0] if " Type " in disease_name else disease_name
                
                # Skip if we've seen this category before
                if category in seen_categories:
                    continue
                    
                # Add to seen categories
                seen_categories.add(category)
                    
                # Add this disease to results
                prediction_results.append({
                    "id": i,
                    "name": disease_name,
                    "probability": float(predictions[i])
                })
                
                # Stop when we have 5 diseases
                if len(prediction_results) >= 5:
                    break
            
            # If we don't have enough diseases, try again including generic conditions
            if len(prediction_results) < 5:
                for i in top_indices:
                    if len(prediction_results) >= 5:
                        break
                        
                    disease_name = get_disease_name(i)
                    category = disease_name.split(" Type ")[0] if " Type " in disease_name else disease_name
                    
                    # Skip if already seen
                    if category in seen_categories:
                        continue
                        
                    seen_categories.add(category)
                    prediction_results.append({
                        "id": i,
                        "name": disease_name,
                        "probability": float(predictions[i])
                    })
            
            print(f"Returning {len(prediction_results)} predictions")
            return JsonResponse({"predictions": prediction_results})
            
        print("Error: Predictions returned None")
        return JsonResponse({"error": "Error making predictions"}, status=400)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": f"Server error: {str(e)}"}, status=500)
