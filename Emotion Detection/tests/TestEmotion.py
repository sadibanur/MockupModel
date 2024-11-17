import pickle

# Load the trained model
import joblib
import pandas as pd

with open("/Users/sadibanoor/Desktop/2022/Fall'22/Research:CSC492/MockupModel/Emotion Detection/models/random_forest.pkl", 'rb') as model_file:
    model = joblib.load(model_file)

    print(type(model))

# Function to get user input
def get_user_input():
    # Get heart rate, HRV, and EEG values from the user
    HR_mean = float(input("Enter HR_mean (e.g., 80): "))  # Heart rate mean
    HRV = float(input("Enter HRV (e.g., 20): "))  # Heart rate variability
    EEG_Alpha = float(input("Enter EEG Alpha value (e.g., 3.5): "))
    EEG_Beta = float(input("Enter EEG Beta value (e.g., 4.0): "))
    EEG_Theta = float(input("Enter EEG Theta value (e.g., 2.5): "))

    # Return the input as a DataFrame with the correct feature names
    input_data = pd.DataFrame([[HR_mean, HRV, EEG_Alpha, EEG_Beta, EEG_Theta]],
                              columns=['HR_mean', 'HRV', 'EEG_Alpha', 'EEG_Beta', 'EEG_Theta'])
    return input_data


# Get input from the user
input_data = get_user_input()

# Make a prediction
prediction = model.predict(input_data)

# Output the result
print(f"The predicted emotion is: {prediction[0]}")
