from model_features import FEATURE_NAMES
from data import preprocessed_symptoms as original_symptoms

def get_formatted_symptoms():
    """Returns the list of symptoms with formatting that matches the model's expectations"""
    return FEATURE_NAMES

def map_symptom(symptom):
    """Maps an input symptom to the correctly formatted version expected by the model"""
    symptom_lower = symptom.lower()
    
    # Try direct match first
    for feature in FEATURE_NAMES:
        if feature.lower() == symptom_lower:
            return feature
    
    # Try removing spaces and punctuation
    simplified_symptom = ''.join(c for c in symptom_lower if c.isalnum())
    for feature in FEATURE_NAMES:
        simplified_feature = ''.join(c for c in feature.lower() if c.isalnum())
        if simplified_symptom == simplified_feature:
            return feature
            
    # If no match found, return the original symptom
    print(f"Warning: No mapping found for '{symptom}'")
    return symptom