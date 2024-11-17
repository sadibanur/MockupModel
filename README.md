Emotion Detection Using Physiological Signals


This project aims to create a mockup model for detecting the emotional state of a child with Autism Spectrum Disorder (ASD) using physiological signals such as heart rate (HR), heart rate variability (HRV), and EEG band powers (alpha, beta, theta).
The process involves three main steps:
   1. Simulating physiological data for different emotional states.
   2. Building a machine learning model (Random Forest Classifier).
   3. Predicting emotional states based on input features.

Simulating Data
We simulate physiological data for three emotional states: Calm, Happy, and Anxious. Each state is associated with distinct patterns of heart rate, HRV, and EEG band powers.
  -Heart Rate (HR_mean): Simulated using a normal distribution with distinct means for each emotion.
  -Heart Rate Variability (HRV): Simulated to reflect typical variations (e.g., higher for calm, lower for anxious).
  -EEG Band Powers: Alpha, Beta, and Theta band powers are generated based on patterns observed in neuroscience studies.
  -The generated data is labeled (Calm, Happy, Anxious) and combined into a single dataset.

Building the Model
A Random Forest Classifier is trained to classify the emotional states based on the simulated features.
  -Random Forest Classifier: An ensemble learning algorithm that creates multiple decision trees and aggregates their results.
  -Feature Importance: This shows which features contribute most to the classification task.

Making Predictions
The model is tested on unseen data to predict emotional states and evaluate its performance.
  -The model predicts emotional states (Calm, Happy, Anxious) based on test data.
  -Performance metrics such as accuracy, precision, recall, and F1-score are calculated to assess model effectiveness.

Results
  -The simulated data provides a clear separation between emotional states based on physiological signals.
  -The Random Forest Classifier achieves high accuracy in distinguishing between the states.
  -Feature importance reveals which physiological signals are most critical for emotion detection.

Future Work
This mockup demonstrates the potential of machine learning in emotion detection. Future directions include:
  -Using real physiological data: Collecting and analyzing real-world signals from autistic children.
  -Exploring other algorithms: Neural Networks, Gradient Boosting, or Support Vector Machines.
  -Real-time emotion detection: Implementing algorithms for real-time analysis using wearable devices.
