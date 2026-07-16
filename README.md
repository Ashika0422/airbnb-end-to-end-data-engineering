# 🏠 Airbnb Market Intelligence Platform

> **An End-to-End Data Engineering, Analytics & Machine Learning Platform for Airbnb Market Intelligence**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-orange?logo=pandas)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-blue?logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Project Overview

The **Airbnb Market Intelligence Platform** is an end-to-end data engineering and analytics solution designed to transform raw Airbnb datasets into actionable business intelligence.

The platform demonstrates the complete data lifecycle, including automated data ingestion, data profiling, cleaning, feature engineering, analytical data warehousing, exploratory data analysis, statistical testing, machine learning, and interactive dashboard development.

Rather than focusing only on data analysis, this project emphasizes modern **Data Engineering practices** by building a scalable analytical pipeline capable of supporting business decision-making.

The final solution provides interactive visualizations, pricing analytics, neighbourhood intelligence, host performance analysis, and machine learning-based price prediction through a professional Streamlit dashboard.

# 🚀 Features

## 📥 Data Engineering

- Automated data ingestion pipeline
- Multi-file dataset integration
- Data profiling and quality assessment
- Missing value treatment
- Duplicate detection
- Data validation
- Feature engineering
- ETL workflow automation
- SQLite analytical warehouse
- Star schema design

---

## 📊 Analytics

- Exploratory Data Analysis (EDA)
- Pricing trend analysis
- Room type analysis
- Property type analysis
- Host analytics
- Neighbourhood intelligence
- Availability analysis
- Review analytics
- Interactive business KPIs

---

## 📈 Statistical Analysis

- Descriptive statistics
- Correlation analysis
- Distribution analysis
- Feature relationships
- Business interpretation of findings

---

## 🤖 Machine Learning

- Price prediction model
- Feature importance analysis
- Model evaluation
- Performance metrics

Algorithms Tested

- Linear Regression
- Random Forest Regressor

Evaluation Metrics

- MAE
- RMSE
- R² Score

---

## 💻 Interactive Dashboard

Professional Streamlit dashboard including:

- Executive Summary
- Interactive Filters
- KPI Cards
- Market Analytics
- Neighbourhood Dashboard
- Host Analysis
- Machine Learning Results
- Business Insights
- Downloadable Reports

  <p align="center">
  <img src="dashboard/assets/dashboard1.png" alt="Airbnb Dashboard" width="900">
  </p>
  <p align="center">
  <img src="dashboard/assets/dashboard2.png" alt="Airbnb Dashboard" width="900">
  </p>
  <p align="center">
  <img src="dashboard/assets/dashbaord3.png" alt="Airbnb Dashboard" width="900">
  </p>

# 🏗️ System Architecture

```
                Raw Airbnb CSV Files
                        │
                        ▼
              Data Ingestion Pipeline
                        │
                        ▼
            Data Profiling & Validation
                        │
                        ▼
          Data Cleaning & Transformation
                        │
                        ▼
            Feature Engineering Layer
                        │
                        ▼
             SQLite Data Warehouse
                        │
                        ▼
        Exploratory Data Analysis (EDA)
                        │
                        ▼
          Statistical Data Analysis
                        │
                        ▼
          Machine Learning Pipeline
                        │
                        ▼
      Interactive Streamlit Dashboard
                        │
                        ▼
            Business Decision Support
```

The project follows a modular architecture that separates each phase of the data engineering lifecycle, enabling maintainability, scalability, and future enhancements.

# 📂 Project Structure

```
Airbnb-Data-Engineering/
│
├── app.py
│
├── assets/
│   ├── pipeline.png
│   ├── dashboard.png
│   └── logo.png
│
├── components/
│   ├── cards.py
│   ├── filters.py
│   ├── footer.py
│   ├── loader.py
│   └── charts.py
│
├── pages/
│   ├── 1_Dataset.py
│   ├── 2_Price_Analytics.py
│   ├── 3_Neighbourhood.py
│   ├── 4_Host_Analysis.py
│   ├── 5_Machine_Learning.py
│   └── 6_Business_Insights.py
│
├── src/
│   ├── ingestion.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── warehouse.py
│   ├── eda.py
│   ├── statistics.py
│   ├── model.py
│   └── dashboard.py
│
├── database/
│   └── airbnb.db
│
├── models/
│   ├── random_forest.pkl
│   ├── scaler.pkl
│   └── feature_importance.csv
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── transformed/
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

# 🛠 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python 3.11 |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Machine Learning | Scikit-Learn |
| Data Visualization | Plotly Express |
| Dashboard | Streamlit |
| Statistical Analysis | SciPy |
| IDE | Visual Studio Code |
| Version Control | Git & GitHub |

---

### Libraries Used

- pandas
- numpy
- matplotlib
- plotly
- seaborn
- scipy
- scikit-learn
- sqlite3
- streamlit
- joblib

# 📊 Dataset

This project utilizes the publicly available Airbnb Open Data.

### Files Used

| Dataset | Description |
|----------|-------------|
| listings.csv | Property listing information |
| calendar.csv | Daily availability and pricing |
| reviews.csv | Customer reviews |
| neighbourhoods.csv | Geographical neighbourhood data |

---

### Dataset Statistics

| Dataset | Records |
|----------|---------|
| Listings | 30,259 |
| Calendar | 11,152,576 |
| Reviews | 990,170 |
| Neighbourhoods | 230 |

---

### Key Attributes

- Listing ID
- Host ID
- Price
- Room Type
- Property Type
- Availability
- Number of Reviews
- Review Ratings
- Latitude
- Longitude
- Accommodates
- Bedrooms
- Beds

# ⚙ Data Engineering Pipeline

The project follows a structured ETL pipeline.

```
Raw CSV Files
        │
        ▼
Data Ingestion
        │
        ▼
Data Profiling
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
SQLite Data Warehouse
        │
        ▼
Analytics Layer
        │
        ▼
Machine Learning
        │
        ▼
Interactive Dashboard
```

### Pipeline Stages

- Automated CSV ingestion
- Schema validation
- Missing value handling
- Duplicate removal
- Feature creation
- Data transformation
- Warehouse loading
- Dashboard visualization

  <p align="center">
  <img src="dashboard/assets/pipeline.png" alt="Airbnb Dashboard" width="900">
  </p>

# 🗄 Data Warehouse Design

The analytical warehouse is implemented using SQLite.

A dimensional star schema was designed to support efficient analytical queries.

## Fact Table

- fact_listings

Contains

- Listing ID
- Host ID
- Price
- Reviews
- Rating
- Availability
- Occupancy Features

---

## Dimension Tables

### dim_host

- Host ID
- Host Name
- Host Since
- Host Experience

---

### dim_listing

- Listing ID
- Room Type
- Property Type
- Bedrooms
- Beds

---

### dim_neighbourhood

- Neighbourhood
- Location Information

The warehouse significantly improves analytical query performance and separates transactional data from analytical reporting.

# 📈 Exploratory Data Analysis

Several exploratory analyses were performed to understand Airbnb market behaviour.

### Analyses Performed

- Price Distribution
- Property Type Distribution
- Room Type Analysis
- Rating Distribution
- Availability Trends
- Review Distribution
- Neighbourhood Pricing
- Host Performance
- Correlation Analysis

### Key Findings

- Entire homes have the highest average prices.
- Listings with higher ratings generally receive more reviews.
- Price varies significantly across neighbourhoods.
- Availability influences estimated revenue potential.

# 📊 Statistical Analysis

Statistical techniques were applied to validate business observations.

### Methods

- Descriptive Statistics
- Correlation Matrix
- Distribution Analysis
- Feature Relationships

### Business Insights

- Strong relationships exist between room type and price.
- Review scores positively influence listing popularity.
- Host experience contributes to better customer ratings.
- Pricing patterns differ considerably across neighbourhoods.

The statistical analysis provides evidence-based support for the business recommendations generated by the platform.


# 🤖 Machine Learning

## Objective

The machine learning component predicts Airbnb listing prices based on property characteristics, location, availability, and review information.

---

## Feature Engineering

The following engineered features were used:

- Price Per Person
- Host Experience
- Availability Ratio
- Review Density
- Bedrooms
- Accommodates
- Number of Reviews
- Review Score Rating

---

## Models Evaluated

| Model | Purpose |
|--------|---------|
| Linear Regression | Baseline model |
| Random Forest Regressor | Final prediction model |

---

## Model Evaluation

Evaluation metrics include:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The Random Forest model achieved the best predictive performance and was selected for deployment within the dashboard.

---

## Business Value

The prediction model helps estimate competitive listing prices based on property characteristics, supporting hosts in pricing decisions and market analysis.

# 📊 Interactive Dashboard

The project includes a professional Streamlit dashboard designed for interactive business intelligence.

## Dashboard Pages

### 🏠 Home Dashboard

- Executive KPIs
- Market Overview
- Summary Metrics
- Pipeline Overview

---

### 📂 Dataset Explorer

- Dataset Summary
- Missing Values
- Data Types
- Sample Records

---

### 📈 Price Analytics

- Price Distribution
- Room Type Analysis
- Property Type Analysis
- Price Comparison

---

### 📍 Neighbourhood Analysis

- Interactive Map
- Top Neighbourhoods
- Price by Location
- Rating Comparison

---

### 👤 Host Analysis

- Host Experience
- Listing Distribution
- Host Performance
- Host Statistics

---

### 🤖 Machine Learning

- Model Performance
- Prediction Results
- Feature Importance
- Evaluation Metrics

---

### 💼 Business Insights

- Executive Recommendations
- Market Trends
- Revenue Opportunities
- Strategic Insights

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Airbnb-Market-Intelligence.git

cd Airbnb-Market-Intelligence
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

# ▶ Running the Project

## Step 1

Run Data Ingestion

```bash
python src/ingestion.py
```

---

## Step 2

Run Data Cleaning

```bash
python src/preprocessing.py
```

---

## Step 3

Run Feature Engineering

```bash
python src/feature_engineering.py
```

---

## Step 4

Build SQLite Warehouse

```bash
python src/warehouse.py
```

---

## Step 5

Run EDA

```bash
python src/eda.py
```

---

## Step 6

Run Statistical Analysis

```bash
python src/statistics.py
```

---

## Step 7

Train Machine Learning Model

```bash
python src/model.py
```

---

## Step 8

Launch Dashboard

```bash
streamlit run app.py
```

# 📈 Results

## Data Engineering

- Successfully integrated multiple Airbnb datasets
- Automated ETL workflow
- Built SQLite analytical warehouse
- Created engineered features

---

## Analytics

- 30K+ Listings Analysed
- 990K+ Reviews Processed
- 230 Neighbourhoods Explored

---

## Dashboard

- Interactive KPI Dashboard
- Dynamic Filtering
- Downloadable Reports
- Business Intelligence Visualizations

---

## Machine Learning

- Successfully trained and evaluated predictive pricing models
- Feature importance analysis completed
- Model integrated into dashboard

# 🚀 Future Improvements

Possible future enhancements include:

- PostgreSQL Integration
- Apache Airflow ETL Automation
- Docker Deployment
- Cloud Deployment (AWS / Azure)
- Real-Time Data Streaming
- Time Series Forecasting
- NLP Analysis of Reviews
- LLM-Based Market Insights
- REST API Integration

# 📜 License

This project is released under the MIT License.

Feel free to use this project for educational and research purposes.

See the LICENSE file for additional information.

# 👩‍💻 Author

## Ashika Chamodi

B.Sc. (Hons) Computer Science (Data Science)

University of Kelaniya

Sri Lanka

---


⭐ If you found this project useful, consider giving it a star on GitHub!
