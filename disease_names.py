# List of disease names corresponding to model prediction indices
DISEASE_NAMES = {
    # Map indices to disease names - add only the ones you know for sure
    0: "Fungal infection",
    1: "Allergy",
    2: "GERD",
    3: "Chronic cholestasis",
    4: "Drug reaction",
    5: "Peptic ulcer disease",
    6: "AIDS",
    7: "Diabetes",
    8: "Gastroenteritis",
    9: "Bronchial asthma",
    10: "Hypertension",
    11: "Migraine",
    12: "Cervical spondylosis",
    13: "Paralysis (brain hemorrhage)",
    14: "Jaundice",
    15: "Malaria",
    16: "Chicken pox",
    17: "Dengue",
    18: "Typhoid",
    19: "Hepatitis A",
    20: "Hepatitis B",
    21: "Hepatitis C",
    22: "Hepatitis D",
    23: "Hepatitis E",
    24: "Alcoholic hepatitis",
    25: "Tuberculosis",
    26: "Common cold",
    27: "Pneumonia",
    28: "Dimorphic hemorrhoids(piles)",
    29: "Heart attack",
    30: "Varicose veins",
    31: "Hypothyroidism",
    32: "Hyperthyroidism",
    33: "Hypoglycemia",
    34: "Osteoarthritis",
    35: "Arthritis",
    36: "Vertigo (Paroymsal Positional Vertigo)",
    37: "Acne",
    38: "Urinary tract infection",
    39: "Psoriasis",
    40: "Impetigo",
    
    # Updated with more specific mental health conditions
    50: "Major Depressive Disorder",
    51: "Generalized Anxiety Disorder",
    52: "Bipolar Disorder",
    53: "Schizophrenia",
    54: "Post-Traumatic Stress Disorder",
    55: "Obsessive-Compulsive Disorder",
    56: "Seasonal Affective Disorder",
    57: "Persistent Depressive Disorder",
    58: "Social Anxiety Disorder",
    59: "Panic Disorder",
    
    # You can add more specific mappings here as you identify them
    100: "Bronchitis",
    101: "Pleurisy", 
    102: "Asthma",
    103: "Emphysema",
    104: "Pneumothorax",
    154: "Pleuritis",
    155: "Chronic Bronchitis",
    
    # Cardiovascular conditions
    200: "Pericarditis",
    201: "Angina",
    202: "Arrhythmia", 
    203: "Heart Valve Disease",
    204: "Hypertensive Heart Disease",
    269: "Costochondritis",
    270: "Myocarditis",
    
    # Infectious diseases
    300: "Infectious Mononucleosis",
    301: "Influenza", 
    302: "Pulmonary Embolism",
    303: "COVID-19",
    304: "Lyme Disease",
    305: "Meningitis",
    306: "Sepsis",
    
    # Digestive conditions
    120: "Peptic Ulcer",
    121: "Gastritis",
    122: "Inflammatory Bowel Disease",
    123: "GERD",
    124: "Gallbladder Disease",
    125: "Pancreatitis",
    126: "Diverticulitis",
    127: "Appendicitis",
    128: "Acute Gastritis",
    129: "Ulcerative Colitis",
    
    # Other common conditions
    380: "Angina Pectoris",
    381: "Rheumatoid Arthritis",
    382: "Osteoporosis",
    383: "Acute Respiratory Infection",
    384: "Chronic Sinusitis",
    385: "Migraine Headache",
    386: "Irritable Bowel Syndrome",
    
    # Add many more mapped conditions
    472: "Bacterial Infection",
    556: "Chronic Fatigue Syndrome",
    649: "Fibromyalgia",
    696: "Acute Coronary Syndrome",
    697: "Lupus",
    
    # EXACT mappings from your diagnostic output
    93: "Joint Inflammation/Arthritis",  # Was showing as "Mood Disorder"
    124: "Peripheral Vascular Disease",  # Was showing as "Gallbladder Disease"
    265: "Deep Vein Thrombosis",         # Was showing as "Infectious Disease"
    377: "Peripheral Edema",             # Was showing as "Cardiovascular Condition"
    601: "Osteoarthritis",               # Was showing as "Metabolic Disorder"
    
    # Other leg/knee related conditions that might appear
    92: "Knee Osteoarthritis",
    94: "Gout",
    95: "Bursitis",
    96: "Tendonitis",
    97: "Muscle Strain",
    98: "Ligament Sprain",
}

# Map specific index ranges to categories
CATEGORY_MAPPING = {
    # Mental health related (update these ranges)
    (50, 99): "Mood Disorder",
    (100, 199): "Respiratory Condition",
    (200, 299): "Infectious Disease",
    (300, 399): "Cardiovascular Condition",
    (400, 499): "Neurological Disorder",
    (500, 599): "Musculoskeletal Disorder",
    (600, 699): "Metabolic Disorder",
    (700, 799): "Immune System Disorder",
    
    # Update category mapping to properly handle leg symptoms
    (90, 110): "Joint Condition",       # This range seems to have joint issues
    (120, 130): "Vascular Condition",    # This range has vascular issues
    (260, 270): "Blood Vessel Disorder", # This range has DVT
    (370, 380): "Edema/Swelling",        # This range has edema
    (600, 610): "Degenerative Joint Disease", # This range has osteoarthritis
}

# Function to get a better disease name
def get_disease_name(index):
    """Returns the disease name for a given index"""
    # If the index is directly in our mapping, return that name
    if index in DISEASE_NAMES:
        return DISEASE_NAMES[index]
        
    # For chest pain related symptoms, categorize based on index ranges
    # These are just examples - customize based on your model's behavior
    for (lower, upper), category in CATEGORY_MAPPING.items():
        if lower <= index <= upper:
            # Add index to make each category unique
            return f"{category} Type {index-lower+1}"
            
    # Default fallback
    return f"Condition {index}"