**Ford Car Price Predictor 🚗💰**

A Machine Learning web app to predict Ford car prices based on features like model, transmission, mileage, fuel type, tax, MPG, and engine size.

💻 Try it live: https://fordcarpriceprediction-kr3dvwr6akkvugfrfghync.streamlit.app/

Project Overview

Cleaned and preprocessed the dataset (handled missing values and duplicates).

Encoded categorical features using OneHotEncoding.

Scaled numeric features for better model performance.

Explored relationships between features and target variable using EDA.

Model

Algorithm: Linear Regression

Train/Test Split: 67% train / 33% test

Performance: R² Score ≈ 83%

Features Used

Categorical: Model, Transmission, Fuel Type

Numerical: Year, Mileage, Tax, MPG, Engine Size

Technologies & Libraries

Python 3.x

Pandas, NumPy

Scikit-learn

Matplotlib, Seaborn

Streamlit (for web deployment)

How to Use

Open the app: Ford Car Price Predictor

Enter the details of your Ford car (year, mileage, tax, MPG, engine size, model, transmission, fuel type).

Click Predict Price to get the estimated car price.

Project Files

app.py → Streamlit app

car_price_model.pkl → Trained Linear Regression model

scaler.pkl → StandardScaler for numeric features

label_encoders.pkl → Encoders for categorical features

requirements.txt → Dependencies for deployment

✅ Deployed live on Streamlit Cloud
