import joblib

# Function to load the trained machine learning model
def load_model(model_path):
    return joblib.load(model_path)

# Function to make predictions using the loaded model
def predict_email(features, model):
    # Assuming features is a list of extracted features and model is the loaded model
    return model.predict([features])
