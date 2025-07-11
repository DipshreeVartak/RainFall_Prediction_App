# 🌦️ Rainfall Prediction App

This is a professional **Rainfall Prediction Web Application** built using **Streamlit** and **Machine Learning (Random Forest Classifier)**. The app predicts whether it will rain based on weather conditions such as pressure, dew point, humidity, cloud cover, sunshine, wind direction, and wind speed.

---

## 🚀 Features

* User-friendly web interface built with Streamlit
* Input weather parameters through sidebar controls
* Predicts rainfall as "Rainfall Expected" or "No Rainfall"
* Displays the probability of rainfall occurrence
* Developed using a GridSearchCV-optimized Random Forest Classifier

---

## 📝 Dataset

The model is trained on a custom dataset containing daily weather observations, including:

* Pressure (hPa)
* Dew Point (°C)
* Humidity (%)
* Cloud Cover (%)
* Sunshine (hours)
* Wind Direction (°)
* Wind Speed (km/h)
* Rainfall (Yes/No)

---

## 📂 Project Structure

```
├── app.py
├── rainfall_model.pkl
├── Rainfall.csv
├── README.md
```

---

## 🛠️ How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/DipshreeVartak/RainFall_Prediction_Web_application-.git
cd rainfall-prediction-app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🧪 Model Training (Summary)

* Data cleaning and feature selection
* Handling class imbalance with downsampling
* Hyperparameter tuning using GridSearchCV
* Model evaluation using cross-validation and test data
* Final model saved using pickle: `rainfall_model.pkl`

---

## 💡 Example Inputs

| Pressure | Dew Point | Humidity | Cloud | Sunshine | Wind Direction | Wind Speed |
| -------- | --------- | -------- | ----- | -------- | -------------- | ---------- |
| 1015.9   | 19.9      | 95       | 81    | 0.0      | 40.0           | 13.7       |

---

## 📈 Prediction Output

* 🌧️ Rainfall Expected
* ☀️ No Rainfall
* Probability of Rainfall: e.g., **82.65%**

---
