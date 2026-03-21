
import pandas as pd

# ==============================
# 1. Load Dataset
# ==============================
data = pd.read_excel(
    r"C:\Users\SAJLE\Downloads\employee_hr_dataset_2000_rows.xlsx"
)

# ==============================
# 2. Data Understanding
# ==============================
print("Dataset Shape:", data.shape)
print("\nColumn Names:\n", data.columns)
print("\nData Types:\n", data.dtypes)

# ==============================
# 3. Missing Value Handling
# ==============================

# Fill Age with median
data['Age'].fillna(data['Age'].median(), inplace=True)

# Fill Salary with median
data['Salary'].fillna(data['Salary'].median(), inplace=True)

# Drop rows where Experience is missing
data.dropna(subset=['Experience'], inplace=True)

print("\nMissing Values After Cleaning:\n", data.isnull().sum())

# ==============================
# 4. Department-wise Salary Analysis
# ==============================
dept_salary = data.groupby('Department')['Salary'].mean().round(2)
print("\nDepartment-wise Average Salary:\n", dept_salary)

# ==============================
# 5. Department-wise Attrition Analysis
# ==============================
attrition_dept = (
    data[data['Attrition'] == 'Yes']
    .groupby('Department')
    .size()
)
print("\nDepartment-wise Attrition Count:\n", attrition_dept)

# ==============================
# 6. Experience-Based Categorization
# ==============================
print("\nExperience Summary:\n",
      data['Experience'].agg(['min', 'max', 'median']))

bins = [0, 2, 7, 40]
labels = ['Fresher', 'Mid', 'Senior']

data['Experience_Category'] = pd.cut(
    data['Experience'],
    bins=bins,
    labels=labels
)

print("\nExperience Category Distribution:\n",
      data['Experience_Category'].value_counts())

# ==============================
# 7. Performance vs Salary
# ==============================
perf_salary = data.groupby('Performance_Rating')['Salary'].mean()
print("\nPerformance Rating vs Average Salary:\n", perf_salary)

# ==============================
# 8. Time-Based Analysis
# ==============================
data['Joining_Year'] = data['Joining_Date'].dt.year

recent_hires = data[data['Joining_Year'] > 2020].shape[0]
print("\nEmployees Joined After 2020:", recent_hires)

# ==============================
# 9. High Earner Identification
# ==============================

# Department-wise average salary for each row
data['Dept_Avg_Salary'] = (
    data.groupby('Department')['Salary']
    .transform('mean')
)

# Salary level classification
data['Salary_Level'] = data.apply(
    lambda row: 'High'
    if row['Salary'] > row['Dept_Avg_Salary']
    else 'Normal',
    axis=1
)

print("\nSample Salary Level Data:\n",
      data[['Name', 'Department', 'Salary',
            'Dept_Avg_Salary', 'Salary_Level']].head())

# ==============================
# 10. Export Final Report
# ==============================
data.to_excel("HR_Analytics_Final_Report.xlsx", index=False)

print("\n✅ HR Analytics Final Report Generated Successfully")
