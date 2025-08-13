import os
import sys
import pickle
import pandas as pd
import traceback
import numpy as np
from symptom_mapping import get_formatted_symptoms, map_symptom

# Get the formatted symptoms list
formatted_symptoms = get_formatted_symptoms()
print(f"Loaded {len(formatted_symptoms)} formatted symptoms")

# ===== Load the trained model =====
def load_model(model_path):
    try:
        # Try multiple locations to find the model
        locations = [
            model_path,
            os.path.join(os.path.dirname(os.path.abspath(__file__)), model_path),
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), model_path)
        ]
        
        for loc in locations:
            if os.path.exists(loc):
                print(f"Found model at: {loc}")
                with open(loc, 'rb') as f:
                    model = pickle.load(f)
                print("✅ Model loaded successfully")
                return model
                
        print(f"❌ ERROR: Model file not found in any location")
        return None
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        traceback.print_exc()
        return None

# ===== Convert matched symptoms to binary vector using correct format =====
def convert_to_binary_vector(matched_symptoms, symptom_list):
    try:
        binary_vector = [0] * len(symptom_list)
        matched_count = 0
        
        for item in matched_symptoms:
            try:
                # Extract symptom name
                if isinstance(item, (list, tuple)) and len(item) >= 1:
                    symptom = item[0]
                elif isinstance(item, str):
                    symptom = item
                else:
                    continue
                
                # Map the symptom to the correct format
                formatted_symptom = map_symptom(symptom)
                
                # Set the binary vector
                if formatted_symptom in symptom_list:
                    index = symptom_list.index(formatted_symptom)
                    binary_vector[index] = 1
                    matched_count += 1
                    print(f"✓ Matched '{symptom}' → '{formatted_symptom}'")
                
            except Exception as e:
                print(f"Error processing symptom {item}: {str(e)}")
        
        print(f"✅ Successfully matched {matched_count} out of {len(matched_symptoms)} symptoms")
        return binary_vector
    except Exception as e:
        print(f"❌ Error converting symptoms: {str(e)}")
        traceback.print_exc()
        return [0] * len(symptom_list)

# ===== Main function to get predictions =====
def get_prediction(matched_symptoms, model_path='LR-83.pkl'):
    try:
        print("\n==== SYMPTOM DIAGNOSTICS ====")
        print(f"Processing {len(matched_symptoms)} symptoms:")
        for symptom in matched_symptoms:
            if isinstance(symptom, tuple):
                print(f"- '{symptom[0]}'")
            else:
                print(f"- '{symptom}'")
        
        print(f"Starting prediction with {len(matched_symptoms)} symptoms")
        model = load_model(model_path)
        
        if not model:
            raise Exception("Failed to load model")
            
        # Convert to binary vector using correctly formatted symptoms
        binary_vector = convert_to_binary_vector(matched_symptoms, formatted_symptoms)
        
        # Create DataFrame with exactly matching column names
        new_data = pd.DataFrame([binary_vector], columns=formatted_symptoms)
        
        # Make predictions
        if hasattr(model, 'predict_proba'):
            predictions = model.predict_proba(new_data)[0]
        else:
            predictions = model.predict(new_data)
        
        print("✅ Prediction generated successfully")
        
        print("\nSymptom matches in binary vector:")
        matched_count = 0
        for i, val in enumerate(binary_vector):
            if val == 1:
                print(f"✓ '{formatted_symptoms[i]}' is active")
                matched_count += 1
        print(f"Total active symptoms in vector: {matched_count}")
        
        print("\nTop 5 predictions:")
        top_indices = sorted(range(len(predictions)), 
                           key=lambda i: predictions[i], 
                           reverse=True)[:5]
        for i, idx in enumerate(top_indices):
            print(f"#{i+1}: Index {idx}: {predictions[idx]*100:.1f}%")
            
        return predictions
    except Exception as e:
        print(f"❌ Error in prediction: {str(e)}")
        traceback.print_exc()
        return None
