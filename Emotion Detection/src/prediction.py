import pandas as pd
import joblib

# Load the trained model
model = joblib.load('models/random_forest.pkl')

# Example new data for prediction
new_data = pd.DataFrame({
    'HR_mean': [72, 88],
    'HRV': [48, 38],
    'EEG_Alpha': [11, 8],
    'EEG_Beta': [9, 14],
    'EEG_Theta': [6, 4]
})

# Make predictions
predictions = model.predict(new_data)
print("Predictions:")
for i, pred in enumerate(predictions):
    print(f"Sample {i + 1}: {pred}")
