import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 1. LOAD DATA
# ==============================
data = pd.read_excel(r"C:\Users\SAJLE\Downloads\Dataset2.xlsx")

# ==============================
# 2. DATA UNDERSTANDING
# ==============================
print("Dataset Shape:", data.shape)
print("\nColumn Info:\n")
print(data.info())

# Check null values
print("\nMissing Values:\n", data.isnull().sum())

# 👉 Insight:
# Postal Code column has 12 missing values.
# Since it does not affect sales or profit analysis, we ignore it.

# ==============================
# 3. DATA CLEANING
# ==============================
print("\nDuplicate Rows:", data.duplicated().sum())

data.drop_duplicates(inplace=True)

# 👉 Insight:
# Found 1 duplicate row → removed to maintain data accuracy.

# ==============================
# 4. KPI ANALYSIS
# ==============================
total_sales = data['Sales'].sum()
max_sales = data['Sales'].max()
min_sales = data['Sales'].min()
total_orders = data['Order ID'].nunique()

print("\n===== KPI METRICS =====")
print("Total Sales:", total_sales)
print("Max Sales:", max_sales)
print("Min Sales:", min_sales)
print("Total Orders:", total_orders)

# 👉 Insights:
# - Total Sales: 2,261,255 → strong revenue
# - Max Sales: 22,638 → few high-value orders
# - Min Sales: 0.44 → very small transactions exist
# - Orders: 4922 → large customer base

# ==============================
# 5. REGION-WISE ANALYSIS
# ==============================
region = data.groupby('Region')['Sales'].sum().sort_values()

print("\nRegion Wise Sales:\n", region)

# 👉 Insight:
# - West region has highest sales
# - South region has lowest sales
# 👉 Recommendation:
# Increase marketing & promotions in South region

# ==============================
# 6. STATE-WISE ANALYSIS
# ==============================
state = data.groupby('State')['Sales'].sum().sort_values()

print("\nState Wise Sales:\n", state)

# 👉 Insight:
# - North Dakota has very low sales (~919)
# - California generates highest revenue
# 👉 Recommendation:
# Improve performance in low-performing states

# ==============================
# 7. CITY-WISE ANALYSIS
# ==============================
city = data.groupby('City')['Sales'].sum().reset_index(name='Total_Sales')

print("\nCity Wise Sales:\n", city.sort_values(by='Total_Sales'))

# 👉 Insights:
# - New York City → highest sales (~252K)
# - Abilene → very low sales (~1.39)
# 👉 Recommendation:
# Focus marketing on underperforming cities

# ==============================
# 8. CATEGORY ANALYSIS
# ==============================
category = data.groupby('Category')['Sales'].sum().reset_index()

print("\nCategory Sales:\n", category)

# 👉 Insight:
# Identify best performing category for business focus

# ==============================
# 9. TOP PRODUCTS
# ==============================
top_products = data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products:\n", top_products)

# 👉 Insight:
# Few products generate majority of revenue

# ==============================
# 10. CUSTOMER ANALYSIS
# ==============================
top_customers = data.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False)

print("\nTop Customers:\n", top_customers.head(10))

# 👉 Insight:
# Some customers contribute heavily to total sales
# 👉 Recommendation:
# Target them with loyalty programs

# ==============================
# 11. TIME SERIES ANALYSIS
# ==============================
data['Order Date'] = pd.to_datetime(data['Order Date'])

monthly_sales = data.groupby(data['Order Date'].dt.month)['Sales'].sum()

print("\nMonthly Sales:\n", monthly_sales)

# 👉 Insight:
# Identify peak months for sales

plt.plot(monthly_sales.index, monthly_sales.values)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()

# ==============================
# 12. VISUALIZATION
# ==============================

# Category Bar Chart
sns.barplot(x='Category', y='Sales', data=category)
plt.title("Category Wise Sales")
plt.show()

# 👉 Insight:
# Compare category performance visually

# Pie Chart (Region)
region = data.groupby('Region')['Sales'].sum()

plt.pie(region.values, labels=region.index, autopct='%1.1f%%')
plt.title("Region Wise Sales Distribution")
plt.show()

# 👉 Insight:
# West dominates overall sales share

# Histogram
plt.hist(data['Sales'], bins=5)
plt.title("Sales Distribution")
plt.show()

# 👉 Insight:
# Most sales are small, few large transactions

# ==============================
# 13. CORRELATION HEATMAP
# ==============================
corr = data.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 👉 Insight:
# Shows relationship between sales, profit, discount etc.