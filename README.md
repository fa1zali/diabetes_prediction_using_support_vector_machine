### Date created
3rd Sep 2022

### Project Title
**Diabetes Prediction using ML**

### Description
Support Vector Machine is a supervised classification algorithm where we draw a line between two different categories to differentiate between them.

For this project, we will be building a machine learning model to classify whether the person is a *Diabetic* or a *Non-Diabetic* based on certain diagnostic measurements included in the dataset provided by the National Institute of Diabetes and Digestive and Kidney Diseases. Our goal is to work through this notebook by collecting data, preprocessing it, splitting it into testing and training datasets, train the model and evaluate the accuracy of our model.

**API**

We have also created an API using FastAPI for users to interact with.
You can run the model using uvicorn on your local machine and test the API, refer to diabetes_api.py & api_testing.py.

Also the API is deployed on Heroku with the following URL : https://diabetesmlapi.herokuapp.com/diabetes_prediction

**StreamLit Web App**

We also created a simple web app using Streamlit.
Use the following link to explore: [Diabetes Prediction Web App](https://diabetesmlwebapp.herokuapp.com/)



### Files used
We used the following dataset available on Kaggle to work on this project:

* [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

### Credits
Thanks to Kaggle for teaching me ML :sparkles: :heart: :sparkles:
