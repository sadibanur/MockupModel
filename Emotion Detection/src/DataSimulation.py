import numpy as np
import pandas as pd

# Setting random seed for reproducibility
np.random.seed(42)

# Function to simulate data for each emotion
def generate_emotion_data(label, size, hr_mean, hr_std, hrv_mean, hrv_std, alpha_mean,
                          alpha_std, beta_mean, beta_std, theta_mean, theta_std):
    data = {
        'HR_mean': np.random.normal(hr_mean, hr_std, size),
        'HRV': np.random.normal(hrv_mean, hrv_std, size),
        'EEG_Alpha': np.random.normal(alpha_mean, alpha_std, size),
        'EEG_Beta': np.random.normal(beta_mean, beta_std, size),
        'EEG_Theta': np.random.normal(theta_mean, theta_std, size),
        'Emotion': [label] * size
    }
    return pd.DataFrame(data)

# Simulating data for emotions
calm_data = generate_emotion_data('Calm', 100, 70, 5, 50, 10, 10, 2, 8, 2, 6, 2)
happy_data = generate_emotion_data('Happy', 100, 75, 5, 45, 8, 12, 2, 10, 2, 5, 2)
anxious_data = generate_emotion_data('Anxious', 100, 85, 5, 35, 8, 7, 2, 15, 3, 4, 2)

# Combine and shuffle
data = pd.concat([calm_data, happy_data, anxious_data]).sample(frac=1).reset_index(drop=True)

# Save to CSV
data.to_csv("/Users/sadibanoor/Desktop/2022/Fall'22/Research:CSC492/MockupModel/Emotion Detection/data/simulated_data.csv", index=False)
print("Simulated data saved to 'data/simulated_data.csv'.")
