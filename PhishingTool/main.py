from email_parser import parse_email
from feature_extractor import extract_features
from phishing_detector import load_model, predict_email

def main():
    # Example raw email content; replace this with actual email content for real tests
    raw_email = """From: "Your Bank" <no-reply@yourbank.fake>
To: victim@example.com
Subject: Urgent account notice
Date: Thu, 25 Feb 2021 13:59:59 -0800
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="simple"

--simple
Content-Type: text/plain; charset=utf-8

Hello, please update your account information immediately at https://phishingsite.fake/update
--simple--
"""

    # Parse the email
    parsed_email = parse_email(raw_email)

    # Extract features
    features = extract_features(parsed_email)

    # Load the machine learning model
    model = load_model('PhishingDetectionTool/models/model.pkl')

    # Make a prediction
    prediction = predict_email(features, model)

    print(f"Prediction: {'Phishing' if prediction[0] == 1 else 'Not Phishing'}")

if __name__ == "__main__":
    main()
