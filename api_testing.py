import json
import requests

# url = "http://127.0.0.1:8000/diabetes_prediction"
# url = "http://ee4f-34-91-223-34.ngrok.io/diabetes_prediction"
url = "https://diabetesmlapi.herokuapp.com/diabetes_prediction"

payload = { 'Pregnancies' : 1,
            'Glucose' : 85,
            'BloodPressure' : 66,
            'SkinThickness' : 29,
            'Insulin' : 0, 
            'BMI' : 26.6,
            'DiabetesPedigreeFunction' : 0.351,
            'Age' : 31
        }

json_payload = json.dumps(payload)

response = requests.post(url, data = json_payload)
print(response)
print(response.text)