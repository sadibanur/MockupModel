
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
data = pd.read_csv("/Users/sadibanoor/Desktop/2022/Fall'22/Research:CSC492/MockupModel/Emotion Detection/data/simulated_data.csv")

# Split into features and labels
X = data[['HR_mean', 'HRV', 'EEG_Alpha', 'EEG_Beta', 'EEG_Theta']]
y = data['Emotion']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the Random Forest model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save the trained model
joblib.dump(clf, "/Users/sadibanoor/Desktop/2022/Fall'22/Research:CSC492/MockupModel/Emotion Detection/models/random_forest.pkl")
print("Model trained and saved to 'models/random_forest.pkl'.")

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
