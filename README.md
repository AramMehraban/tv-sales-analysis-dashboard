# Sales Data Analysis Dashboard

## Project Overview

This project is an end-to-end data analysis solution that explores the relationship between advertising spend and product sales.

It includes:

- Data cleaning
- Exploratory data analysis (EDA)
- Statistical analysis
- Data visualization
- Interactive dashboard built with Streamlit

* The goal is to demonstrate practical data analysis skills suitable for a Junior Data Analyst role.


## Project Goal
This project simulates a real-world business scenario and demonstrates how data-driven insights can support marketing and sales decisions.


## Tools & Technologies
- Python
- Pandas
- NumPy
- Seaborn
- Plotly
- Streamlit
- Matplotlib


## Project Structure
```
sales-analysis-project/
│
├── data/
       └── advertising.csv
├── dashboard/
│       └── app.py
├── src/
│       └── main.py
│       └── reports_generator.py
│       └── reports/
│           └── final_report.pdf
│           └── heatmap.png
│           └── scatter.png
├── requirements.txt
├── .gitignore
├── setup.bat
└── README.md
```

## Key Features

### 1. Data Analysis
- Descriptive statistics
- Correlation analysis
- Distribution analysis

### 2. Data Visualization
- Scatter plots (TV vs Sales)
- Correlation heatmap
- Sales distribution charts

### 3. Interactive Dashboard (Streamlit)
### Built with Streamlit:
- KPI metrics (Total Sales, Average Sales, Max Sales)
- Interactive filters (Sales range slider)
- Dynamic visualizations

## Key Insights
- TV advertising shows the strongest correlation with sales
- Sales distribution is slightly skewed
- Higher advertising spend generally leads to higher sales

## How to Run

### 1. Clone repository
```bash
git clone https://github.com/AramMehraban/tv-sales-analysis-dashboard.git
cd tv-sales-analysis-dashboard
```

### 2. One-click setup (recommended)
```bash
setup.bat
```

### 3. Manual setup (alternative)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 4. Run dashboard
```bash
python -m streamlit run dashboard/app.py
```

# Dashboard Preview

The dashboard includes:

- KPI cards
- Scatter plot visualization
- Correlation heatmap
- Dynamic filtering system

# Skills Demonstrated
- Data Analysis (Pandas, NumPy)
- Data Visualization (Matplotlib, Seaborn, Plotly)
- Dashboard Development (Streamlit)
- Statistical Analysis (Correlation, Distribution)
- Python Automation

# Future Improvements
- Machine Learning regression model for sales prediction
- Deployment on Streamlit Cloud
- Integration with real-time data sources

# Note

This project was developed as part of a personal data analytics portfolio to demonstrate practical skills in Python and data visualization.


## Author

**Created by:** Aram Mehraban  
**Role:** Junior Data Analyst  
**Focus:** Python, Data Analysis, Business Intelligence


## License

This project is for educational and portfolio purposes.