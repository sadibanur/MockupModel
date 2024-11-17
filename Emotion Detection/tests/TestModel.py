import unittest
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

class TestModel(unittest.TestCase):
    def setUp(self):
        # Load the trained model
        self.model = joblib.load("/Users/sadibanoor/Desktop/2022/Fall'22/Research:CSC492/MockupModel/Emotion Detection/models/random_forest.pkl")

    def test_model_load(self):
        # Ensure the model is of the correct type
        self.assertIsInstance(self.model, RandomForestClassifier)

    def test_predictions(self):
        # Example input data
        test_data = pd.DataFrame({
            'HR_mean': [72, 88],
            'HRV': [48, 38],
            'EEG_Alpha': [11, 8],
            'EEG_Beta': [9, 14],
            'EEG_Theta': [6, 4]
        })

        # Make predictions
        predictions = self.model.predict(test_data)
        self.assertEqual(len(predictions), 2)

if __name__ == '__main__':
    unittest.main()
