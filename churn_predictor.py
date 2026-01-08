
import joblib
import numpy as np
import pandas as pd
import json

class ChurnPredictor:

    def __init__(self, model_path='best_churn_model.pkl',
                 preprocessor_path='preprocessing_pipeline.pkl',
                 features_path='feature_names.json'):

        self.model = joblib.load(model_path)
        self.preprocessor = joblib.load(preprocessor_path)

        with open(features_path, 'r') as f:
            self.feature_names = json.load(f)

    def preprocess_input(self, customer_data):
        if not isinstance(customer_data, pd.DataFrame):
            customer_data = pd.DataFrame([customer_data])

        X_processed = self.preprocessor.transform(customer_data)
        return X_processed

    def predict(self, customer_data, return_probability=True):
        X_processed = self.preprocess_input(customer_data)

        if return_probability:
            proba = self.model.predict_proba(X_processed)[0]
            return {
                'churn_probability': float(proba[1]),
                'prediction': int(proba[1] > 0.5),
                'confidence': float(max(proba))
            }
        else:
            prediction = self.model.predict(X_processed)[0]
            return {'prediction': int(prediction)}

    def predict_batch(self, customers_data):
        predictions = []

        for customer in customers_data:
            pred = self.predict(customer)
            predictions.append(pred)

        return predictions
