# **Ford Car Price Predictor** 🚗💰

A **Machine Learning web app** to predict **Ford car prices** based on features like **model, transmission, mileage, fuel type, tax, MPG, and engine size**.  

💻 **Try it live:** [Ford Car Price Predictor](https://fordcarpriceprediction-kr3dvwr6akkvugfrfghync.streamlit.app/)  

---

## **Project Overview**
- **Data Cleaning:** Handled missing values and duplicates  
- **Feature Encoding:** Used **OneHotEncoding** for categorical variables  
- **Scaling:** Standardized numeric features for better model performance  
- **Exploratory Data Analysis (EDA):** Explored relationships between features and target variable  

---

## **Model**
- **Algorithm:** Linear Regression  
- **Train/Test Split:** 67% train / 33% test  
- **Performance:** **R² Score ≈ 83%**  

---

## **Features Used**
- **Categorical:** Model, Transmission, Fuel Type  
- **Numerical:** Year, Mileage, Tax, MPG, Engine Size  

---

## **Technologies & Libraries**
- **Python 3.x**  
- **Pandas, NumPy**  
- **Scikit-learn**  
- **Matplotlib, Seaborn**  
- **Streamlit** (for web deployment)  

---

## **How to Use**
1. Open the app: [Ford Car Price Predictor](https://fordcarpriceprediction-kr3dvwr6akkvugfrfghync.streamlit.app/)  
2. Enter the details of your Ford car (**year, mileage, tax, MPG, engine size, model, transmission, fuel type**)  
3. Click **Predict Price** to get the estimated car price  

---

## **Project Files**
| File | Description |
|------|-------------|
| `app.py` | Streamlit app |
| `car_price_model.pkl` | Trained Linear Regression model |
| `scaler.pkl` | StandardScaler for numeric features |
| `label_encoders.pkl` | Encoders for categorical features |
| `requirements.txt` | Dependencies for deployment |

---

✅ **Deployed live on Streamlit Cloud**  

---

### Optional: Badges for a professional GitHub look
```markdown
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-green)
