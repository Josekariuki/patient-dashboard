# Patient Data EDA & Health Dashboard

An exploratory data analysis and interactive dashboard built on the Pima Indians Diabetes dataset. The project walks through the full data science workflow — loading, cleaning, feature engineering, visualization, and deployment of an interactive web dashboard.

## Overview

This dashboard lets users explore clinical risk factors for diabetes across a patient population. It surfaces distributions, relationships between features, and key population-level metrics through interactive filters and charts.

Built as the foundation project in a structured data science portfolio, with an emphasis on clean, reproducible analysis and clinical interpretability.

## Features

- Interactive filters by age group and diabetes status
- Live KPI cards: patient count, diabetes rate, average glucose, average BMI
- Glucose distribution histogram segmented by outcome
- BMI distribution by age group (box plots)
- Feature correlation heatmap
- Toggleable raw data view

## Tech Stack

- **Python 3.12**
- **Pandas / NumPy** — data manipulation
- **Matplotlib / Seaborn** — exploratory visualization
- **Plotly** — interactive charts
- **Streamlit** — dashboard framework

## Dataset

Pima Indians Diabetes Database (768 patients, 8 clinical features + outcome label). Sourced from the UCI Machine Learning Repository / Kaggle.

Clinical features: pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, and age.

## Project Structure

```
patient-dashboard/
├── data/
│   ├── diabetes.csv             # raw dataset
│   └── diabetes_clean.csv       # cleaned + feature-engineered
├── notebooks/
│   └── 01_eda.ipynb             # exploratory analysis
├── app/
│   └── dashboard.py             # Streamlit dashboard
├── visuals/                     # exported charts
├── requirements.txt
└── README.md
```

## Setup & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/patient-dashboard.git
   cd patient-dashboard
   ```

2. Create and activate an environment (conda recommended):
   ```bash
   conda create -n ds python=3.12 -y
   conda activate ds
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the dashboard:
   ```bash
   streamlit run app/dashboard.py
   ```

   The app opens automatically at `http://localhost:8501`.

## Methodology

**Data cleaning** — Physiologically impossible zero values in glucose, blood pressure, skin thickness, insulin, and BMI were treated as missing data and imputed using column medians (robust to outliers in clinical data).

**Feature engineering** — Derived categorical features including BMI category (WHO classification), glucose range, age group, and a composite risk score combining elevated glucose, high BMI, and older age.

**Exploratory analysis** — Examined feature distributions, class balance, and inter-feature correlations to identify the strongest predictors of diabetes (glucose and BMI emerged as dominant signals, consistent with clinical literature).

## Key Findings

- Glucose level is the single strongest correlate of diabetes outcome.
- BMI and age show clear positive associations with diabetes risk.
- The dataset is moderately imbalanced (~35% positive cases), an important consideration for any downstream predictive modeling.

## Author

Joseph Kariuki — Clinical Medicine graduate and aspiring data scientist, combining clinical domain expertise with practical data science and machine learning skills.

## License

MIT License — free to use and adapt.
