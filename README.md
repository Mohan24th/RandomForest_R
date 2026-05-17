#  House Price Prediction Using Random Forest Regressor

##  Project Overview

This project predicts house prices using Machine Learning.

The model is built using the Random Forest Regressor algorithm and deployed using Streamlit for interactive real-time predictions.

---

#  Features

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Correlation heatmap visualization
- Feature engineering
- One-hot encoding
- Random Forest Regression
- Hyperparameter tuning using GridSearchCV
- Feature importance analysis
- Decision tree visualization
- Streamlit frontend application

---

#  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

#  Dataset

Dataset contains housing-related features such as:
- Area
- Bedrooms
- Bathrooms
- Floors
- Parking
- Air Conditioning
- Furnishing Status
- Preferred Area
- House Price

---

#  Machine Learning Model

Algorithm Used:
## Random Forest Regressor

Why Random Forest Regressor?
- Handles nonlinear relationships
- Reduces overfitting
- Works well with mixed data types
- Provides feature importance
- High prediction accuracy

---

#  Model Evaluation

Metrics Used:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

#  Tree Visualization

The project visualizes individual decision trees from the Random Forest using:

```python
tree.plot_tree()
```

This helps understand:
- Feature splits
- Decision paths
- Tree depth
- Model structure

---

#  Streamlit Application

The Streamlit app allows users to:
- Enter property details
- Predict house prices instantly
- View property summary
- Understand price insights

---

#  Run the Project

## Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

## Run Streamlit App

```bash
streamlit run app.py
```

---

#  Project Structure

```text
project/
│
├── app.py
├── housing.csv
├── house_price_model.pkl
├── model_columns.pkl
├── RandomForestRegressor.ipynb
├── random_forest_tree.png
├── README.md
```

---

#  Future Improvements

- Add advanced UI styling
- Add map-based property location
- Add house image upload
- Deploy on cloud platforms
- Add price trend analysis
- Add explainable AI visualizations

---



Developed as a Machine Learning project using Random Forest Regression and Streamlit deployment.
