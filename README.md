I want to create something useful and this is a bigger project compared to my other ones. Essentially I'm creating a tool that can detect phishing emails via you just paste an email into an input and it can find out if the email is bad or not. Here is stuff in it so far...
email_parser.py:
Parses the raw email stuff to extract important things e.g. headers body URLS.
feature_extractor.py:
Analyzes the parsed email to extract certain features taht determines if an email is a phishing attempt.
phishing_detector.py:
Loads a pre-trained MLM (machine learning model) and uses it to predict whtether an email is phishing based on its features. It loads the MLM from a file (load_model) and uses said loaded model to make predictions based on the extracted features (predict_meail)
model_train.py:
Used for training the MLM using labeled data (UNFINISHED)
Splits the data into training and testing sets. trains a randomforestclassifier and evalutes the accuaracy and then saves the model.
app.py:
This just provides a web interface for users to input email content and get predictions. This is convenient compared to having to look at the terminal all the time (it gets cluttered)
/predict handles the form submission processes the email, extracts features makes a prediction and then returns the result.
The template folder contains index.html that users interact with to submit the emails for analysis.

How to use:
1. Starting the Flask app (go to app.py and run it) This will start the flask server
2. application at http://localhost:5000
3. Open a web browser and go to the sit ^^^
4. Paste an email where the textarea is and then click the analyze email button
5. Email content is then sent to the flask server and is processed by...
- Parsing the email through email_parser.py
- Extracting features using feature_extractor.py
- Predicting whether it's phishing or not using phishing_detector.py
- Should output whether it is phishing or not phishing on the webpage
6. To test other emails, go back to the page (http://localhost:5000) paste a new email and submit again.

Again I'm not finished and a lot of the current code is just testing
