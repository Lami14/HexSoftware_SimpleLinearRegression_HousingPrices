# 🏠 Simple Linear Regression on Housing Prices

## 📌 Overview
This project demonstrates an end-to-end machine learning workflow using Simple Linear Regression to predict housing prices based on the number of rooms.

It covers data loading, preprocessing, model training, evaluation, and visualization using Python.

---

## 🧰 Tech Stack
- Python
- Pandas
- Matplotlib
- Scikit-learn

---

## 📊 Dataset
The project uses a housing dataset (Boston Housing dataset via sklearn) to model the relationship between the number of rooms and house prices.

---

## 📂 Project Structure
```
notebooks/
│   └── housing_regression.ipynb

src/
│   ├── housing_regression.py
│   └── regression_utils.py

requirements.txt
README.md
```

---

## ⚙️ How It Works
1. Load and explore the dataset  
2. Select feature (number of rooms - RM)  
3. Split data into training and testing sets  
4. Train a Linear Regression model  
5. Evaluate using MSE and R² score  
6. Visualize predictions vs actual values  

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
python src/housing_regression.py
```

---

## 📈 Results
- Positive relationship between number of rooms and house prices  
- Model provides a reasonable baseline for prediction  
- Performance evaluated using Mean Squared Error and R² score  

---

## 🧠 Model Formula
y = mx + b

---

## 🔮 Future Improvements
- Use Multiple Linear Regression (more features)
- Apply feature engineering
- Try advanced models (Random Forest, XGBoost)
- Deploy with Streamlit

---

## 📌 Author
Lamla Mhlana 
