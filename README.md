## **Emotion Detection Using Physiological Signals**


This project aims to create a mockup model for detecting the emotional state of a child with Autism Spectrum Disorder (ASD) using physiological signals such as heart rate (HR), heart rate variability (HRV), and EEG band powers (alpha, beta, theta).
The process involves three main steps:
   1. Simulating physiological data for different emotional states.
   2. Building a machine learning model (Random Forest Classifier).
   3. Predicting emotional states based on input features.

### **1. Simulating Data:**

We simulate physiological data for three emotional states: Calm, Happy, and Anxious. Each state is associated with distinct patterns of heart rate, HRV, and EEG band powers.
1. Heart Rate (HR_mean): Simulated using a normal distribution with distinct means for each emotion.
2.   Heart Rate Variability (HRV): Simulated to reflect typical variations (e.g., higher for calm, lower for anxious).
3.   EEG Band Powers: Alpha, Beta, and Theta band powers are generated based on patterns observed in neuroscience studies.
4.   The generated data is labeled (Calm, Happy, Anxious) and combined into a single dataset.

### **2. Building the Model:**

A Random Forest Classifier is trained to classify the emotional states based on the simulated features.
1.   Random Forest Classifier: An ensemble learning algorithm that creates multiple decision trees and aggregates their results.
2.   Feature Importance: This shows which features contribute most to the classification task.

### **3. Making Predictions:**

The model is tested on unseen data to predict emotional states and evaluate its performance.
1.   The model predicts emotional states (Calm, Happy, Anxious) based on test data.
2.   Performance metrics such as accuracy, precision, recall, and F1-score are calculated to assess model effectiveness.

### 4. Results:

1.   The simulated data provides a clear separation between emotional states based on physiological signals.
2.   The Random Forest Classifier achieves high accuracy in distinguishing between the states.
3.   Feature importance reveals which physiological signals are most critical for emotion detection.

### Future Work:

This mockup demonstrates the potential of machine learning in emotion detection. Future directions include:
1.   Using real physiological data: Collecting and analyzing real-world signals from autistic children.
2.   Exploring other algorithms: Neural Networks, Gradient Boosting, or Support Vector Machines.
3.   Real-time emotion detection: Implementing algorithms for real-time analysis using wearable devices.
