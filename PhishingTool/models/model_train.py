import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Path for saving the model
model_directory = 'PhishingDetectionTool/models'
model_path = f'{model_directory}/model.pkl'

# Ensure the directory exists
if not os.path.exists(model_directory):
    os.makedirs(model_directory)

# Example: Dummy data to represent email features and labels
features = [[0, 1], [1, 1], [1, 0], [0, 0]]  # Example features
labels = [0, 1, 1, 0]  # 0 = not phishing, 1 = phishing

# Splitting data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.25, random_state=42)

# Creating the Random Forest classifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)  # Training the model

# Optionally, evaluate the model
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

# Save the trained model to a file
joblib.dump(model, model_path)
