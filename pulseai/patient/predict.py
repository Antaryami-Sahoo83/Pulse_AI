import pickle
import joblib
import pandas as pd


def predict_heart_disease(patient_data):
      with open('patient/aimodels/label_encoders.pkl', 'rb') as file:
            label_encoders = pickle.load(file)
      scaler = joblib.load('patient/aimodels/scaler.pkl')
      model = joblib.load("patient/aimodels/heart_failure_rf_model.pkl")

      categorical_columns = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
      numerical_columns = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']

      patient_data = pd.DataFrame([patient_data])
      for col in numerical_columns:
            patient_data[col] = pd.to_numeric(patient_data[col])
      for col in categorical_columns:
            patient_data[col] = label_encoders[col].transform(patient_data[col])
      print(patient_data)

      # Scale the new data using the previously fitted scaler
      scaled_data = scaler.transform(patient_data)
      # Peredict
      prediction = model.predict(scaled_data)
      print(prediction)
      # Predict using the trained model
      prediction_probability = model.predict_proba(scaled_data)[0][1]
      # print(f'There is {prediction_probability:.0%} chance that the patient has heart disease.')
      if prediction[0]==1:
            pclass = 'Yes'
      else:
            pclass = 'No'
      return {'class': pclass, 'probability': f'{prediction_probability: .0%}'}

