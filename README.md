# Sales Data Analysis Dashboard

## Project Overview
This project is an end-to-end data analysis solution that explores the relationship between advertising spending and product sales.  
It includes data cleaning, statistical analysis, visualization, and an interactive dashboard built with Python.

The goal is to demonstrate practical data analysis skills suitable for a Junior Data Analyst role.



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
│ └── advertising.csv
│
├── dashboard/
│ └── app.py
│
├── src/
│ ├── main.py
│ └── report_generator.py
│
├── reports/
│ ├── scatter.png
│ ├── heatmap.png
│ └── final_report.pdf
│
├── requirements.txt
├── .gitignore
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

### 3. Interactive Dashboard
Built with Streamlit:
- KPI metrics (Total Sales, Average Sales, Max Sales)
- Interactive filters (Sales range slider)
- Dynamic visualizations



## Key Insights
- TV advertising shows the strongest correlation with sales
- Sales distribution is slightly skewed
- Higher advertising spend generally leads to higher sales



## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/AramMehraban/sales-analysis-project.git
cd sales-analysis-project
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run analysis
```bash
python src/main.py
```

### 5. Run dashboard
```bash
streamlit run dashboard/app.py
```

# 📊 Dashboard Preview

#### The dashboard includes:
- Interactive KPI cards
- Scatter plot visualization
- Correlation heatmap
- Dynamic filtering system


# Skills Demonstrated
- Data cleaning & preprocessing
- Statistical analysis (correlation, distribution)
- Data visualization
- Dashboard development
- Python automation


# Future Improvements
- Machine Learning regression model for sales prediction
- Deployment on Streamlit Cloud
- Integration with real-time data sources

##  Author

**Created by:** Aram Mehraban  
**Role:** Junior Data Analyst  
**Focus:** Python, Data Analysis, Power BI, Business Intelligence

# License

This project is for educational and portfolio purposes