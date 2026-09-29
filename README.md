# Employee Attrition Prediction Dashboard

## Project Overview

This project analyzes employee attrition using the IBM HR Analytics Employee Attrition & Performance dataset. It combines exploratory data analysis, machine learning, and an interactive Power BI dashboard to identify patterns associated with employee turnover.

## Objectives

- Clean and prepare employee HR data.
- Explore factors associated with employee attrition.
- Build a machine learning model for binary attrition prediction.
- Evaluate model performance using accuracy, precision, recall, F1-score, and a confusion matrix.
- Build an interactive Power BI dashboard for business-oriented analysis.

## Dataset

The dataset contains **1,470 employee records**.

After data cleaning, the working dataset contains **31 columns**. The following administrative columns were removed:

- `EmployeeCount`
- `EmployeeNumber`
- `Over18`
- `StandardHours`

The dataset contains:

- **1,233** employees who stayed
- **237** employees who left
- Overall attrition rate: **16.12%**
- Missing values: **0**
- Duplicate rows: **0**

> The analysis describes associations observed in the dataset. It does not establish that any particular factor causes employee attrition.

## Exploratory Data Analysis

Several employee characteristics were analyzed, including department, overtime, job satisfaction, monthly income, age, business travel, job role, marital status, and education field.

Some observed patterns include:

- Employees working overtime had an observed attrition rate of **30.53%**, compared with **10.44%** for employees not working overtime.
- Department-level attrition rates were **20.63% for Sales**, **19.05% for HR**, and **13.84% for R&D**.
- Employees aged **18–25** had an observed attrition rate of **35.77%**.
- Employees in the lowest monthly-income group had an observed attrition rate of **21.76%**.

## Machine Learning

### Model

A **Logistic Regression** classifier was used for binary attrition prediction.

The preprocessing workflow included:

- Separating features and target.
- Converting `Attrition` from `Yes/No` to `1/0`.
- Stratified 80/20 train-test split.
- One-hot encoding of categorical variables.
- Logistic Regression classification.

### Baseline Model

The baseline model achieved:

- **Accuracy:** 87.75%
- Attrition recall: **26%**
- Attrition F1-score: **0.40**

The baseline accuracy was relatively high, but the model detected only a minority of actual attrition cases.

### Balanced Model

A second Logistic Regression model used `class_weight="balanced"` to give greater importance to the minority attrition class.

Results:

- **Accuracy:** 75%
- Attrition precision: **0.35**
- Attrition recall: **0.64**
- Attrition F1-score: **0.45**

Confusion matrix:

```text
[[191, 56],
 [ 17, 30]]
```

The balanced model improved recall for employees who actually left, while reducing overall accuracy. This illustrates the trade-off between overall accuracy and minority-class detection in an imbalanced classification problem.

## Power BI Dashboard

The Power BI dashboard contains:

### KPI Cards

- **Total Employees:** 1,470
- **Employees Left:** 237
- **Attrition Rate:** 16.12%

### Visualizations

- Attrition by Department
- Attrition by Job Role
- Attrition by Overtime
- Attrition by Business Travel
- Attrition by Marital Status
- Attrition by Education Field

## Tools & Technologies

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Joblib**
- **Matplotlib**
- **Seaborn**
- **Power BI**
- **Microsoft Excel**

## Project Files

```text
Employee-Attrition-Prediction/
│
├── README.md
├── attrition_analysis.py
├── employee_attrition_model.pkl
├── Employee_Attrition_Prediction_Project_Report.pdf
├── Employee_Attrition_Dashboard.pbix
├── dashboard_screenshot.png
└── data/
    └── HR_Employee_Attrition.xlsx
```

## How to Run the Python Analysis

1. Install Python 3.x.
2. Install the required packages:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl joblib
```

3. Place the Excel dataset in the expected project location.
4. Run:

```bash
python attrition_analysis.py
```

The script performs data preparation, exploratory analysis, model training, and evaluation.

## Limitations

- The dataset is historical and may not represent every organization.
- Associations in the dataset should not be interpreted as causal relationships.
- Logistic Regression is used as a baseline classification approach.
- The attrition class is imbalanced, so accuracy should be considered alongside recall, precision, and F1-score.
- The machine learning model and Power BI dashboard are maintained as separate project components.

## Future Improvements

- Compare Logistic Regression with Random Forest and Gradient Boosting.
- Tune the classification threshold.
- Add model probability predictions to the dashboard.
- Add interactive slicers and more detailed HR segmentation.
- Evaluate the model on newer organizational data.

## Author

**Name:** Chandrakala.C
**Project:** Employee Attrition Prediction Dashboard  
**Type:** Internship Project
