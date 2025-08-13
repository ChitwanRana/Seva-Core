# SEVA: Support for Vital and Essential Aids

SEVA stands for **Support for Vital and Essential Aids**. This project provides free health recommendations using AI-powered symptom analysis. Users can enter their symptoms, select relevant matches, and receive possible conditions to discuss with a healthcare provider. SEVA aims to make essential health guidance accessible to everyone, supporting better awareness and early action for vital health concerns.

## 🌟 Features

- **Natural Language Symptom Analysis**: Enter symptoms in everyday language
- **Intelligent Symptom Matching**: AI-powered matching of user descriptions to medical symptoms
- **Customizable Symptom Selection**: Select and refine matched symptoms for accuracy
- **Medical Condition Predictions**: Machine learning model provides relevant health insights
- **User-Friendly Interface**: Step-by-step guided experience with visual feedback
- **Responsive Design**: Works on desktop and mobile devices
- **Save & Share Results**: Export results as PDF or share with others

## 🔧 Technology Stack

- **Backend**: Django 5.2
- **Machine Learning**: Scikit-learn (Logistic Regression model)
- **NLP Processing**: Custom natural language processing for symptom matching
- **Frontend**: HTML, CSS, JavaScript with Bootstrap 5
- **Database**: SQLite (for development)
- **Environment**: Python virtual environment

## 🚀 Installation & Setup

### Prerequisites

- Python 3.12 or higher
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/ChitwanRana/Seva-Core.git
cd Seva-Core/Seva
```

### Step 2: Create and Activate Virtual Environment

```bash
# On Windows
python -m venv myenv
myenv\Scripts\activate

# On macOS/Linux
python -m venv myenv
source myenv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/

## 🔍 How It Works

1. **Symptom Input**: Users describe their symptoms in natural language
2. **Symptom Matching**: The NLP system matches input to known medical symptoms
3. **Symptom Selection**: Users select which matched symptoms apply to them
4. **Analysis**: The machine learning model analyzes the selected symptoms
5. **Results**: Users receive potential conditions based on their symptoms

## 📋 Project Structure

- `Seva/` - Main project directory
  - `Seva/` - Django project settings
  - `Seva_App/` - Main application code
  - `templates/` - HTML templates
  - `data.py` - Symptom data preprocessing
  - `predict.py` - Machine learning prediction logic
  - `NLPTransformer.py` - Natural language processing for symptom matching
  - `disease_names.py` - Disease name mappings
  - `model_features.py` - Features used by the ML model
  - `LR-83.pkl` - Trained machine learning model

## ⚠️ Disclaimer

SEVA is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 👥 Authors

- Chitwan Rana - Initial work - [ChitwanRana](https://github.com/ChitwanRana)
