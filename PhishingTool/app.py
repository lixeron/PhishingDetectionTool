from flask import Flask, render_template, request, jsonify
from email_parser import parse_email
from feature_extractor import extract_features
from phishing_detector import load_model, predict_email

app = Flask(__name__)

# Load the model once when the app starts
model = load_model('PhishingDetectionTool/models/model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email_content = request.form['email']
        parsed_email = parse_email(email_content)
        features = extract_features(parsed_email)
        prediction = predict_email(features, model)
        result = 'Phishing' if prediction[0] == 1 else 'Not Phishing'
        return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
