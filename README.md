# 🚖 NYC Taxi Statistical Analysis  

Applying statistical methods to explore NYC taxi trip data, based on concepts from "Practical Statistics for Data Scientists (2nd Edition)".

## 📌 Project Overview

This project applies key statistical methods to analyze NYC taxi trip data, using concepts from "Practical Statistics for Data Scientists" (2nd Edition). The analysis covers exploratory data analysis (EDA), hypothesis testing, regression models, resampling methods, and machine learning techniques.

➡️ [Full Statistical Analysis Breakdown](reports/statistical_analysis.md)

The insights and findings are presented through Jupyter notebooks, statistical scripts, and an interactive dashboard.  

---

## 📊 Project Goals

✔️ **Descriptive Statistics** – Analyze distributions of fares, trip distances, and trip durations.  
✔️ **Hypothesis Testing** – Identify factors affecting fare prices and tipping behavior.  
✔️ **Regression Modeling** – Build predictive models for fare estimation.  
✔️ **Clustering Analysis** – Segment customers based on trip behavior.  
✔️ **Data Visualization** – Create interactive dashboards to present insights.  

---

## 📂 Project Structure

```graphql
nyc_taxi_statistics_project/
│── data/                    # Dataset storage
│   ├── raw/                 # Original data
│   ├── processed/           # Cleaned & transformed data
│   ├── nyc_taxi_sample.csv  # A small sample for quick testing
│
│── notebooks/               # Jupyter Notebooks for analysis
│   ├── 01_exploratory_data_analysis.ipynb  # EDA on NYC taxi data
│   ├── 02_probability_theory.ipynb         # Applying probability concepts
│   ├── 03_sampling_hypothesis_testing.ipynb # Statistical inference & testing
│   ├── 04_regression_analysis.ipynb        # Regression models for predictions
│   ├── 05_categorical_data_analysis.ipynb  # Working with categorical features
│   ├── 06_resampling_methods.ipynb         # Bootstrap & cross-validation
│   ├── 07_machine_learning_models.ipynb    # Applying ML on taxi data
│
│── src/                     # Core scripts for data processing and analysis
│   ├── __init__.py          # Makes `src` a Python package
│   ├── data_preprocessing.py # Data cleaning & feature engineering
│   ├── visualization.py      # Functions for data visualization
│   ├── hypothesis_testing.py # Statistical tests implementation
│   ├── regression_models.py  # Regression models and evaluation
│   ├── utils.py              # Utility functions for reusability
│
│── dashboard/               # Interactive data visualization
│   ├── app.py               # Main dashboard application (Flask/Streamlit)
│   ├── plots.py             # Visualization functions
│   ├── layout.py            # Layout structure of the dashboard
│
│── reports/                 # Analysis reports & documentation
│   ├── exploratory_analysis.md # Summary of EDA findings
│   ├── statistical_findings.md # Key insights & hypothesis testing results
│   ├── model_performance.md    # Performance of regression & ML models
|   ├── statistical_analysis.md
│
│── requirements.txt         # List of required Python libraries
│── README.md                # Project overview & instructions
│── .gitignore               # Ignore unnecessary files (datasets, cache, etc.)
|── LICENSE

```

## 🚀 How to Run  

### 1. **Install Dependencies**  

```bash
pip install -r requirements.txt
```

### 2. Run Jupyter Notebooks

```bash
jupyter notebook notebooks/
```

### 3. Run the Dashboard

```bash
python dashboard/app.py
```

---

## 📌 References

- Practical Statistics for Data Scientists (2nd Edition) - Peter Bruce & Andrew Bruce
- NYC Taxi & Limousine Commission (TLC) Dataset - [Official Source](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)