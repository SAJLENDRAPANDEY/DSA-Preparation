# ------------------ Linear Regression ------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load dataset
data = pd.read_excel(r"C:\yash_important data\student_performance_dataset new.xlsx")

print(data.head(5))

# Encode Result column
data['Result'] = data['Result'].map({'Fail': 0, 'Pass': 1})

# Features & Target
X = data[["Hours_Study", "Attendance", "CGPA", "Test_Score"]]
y = data["Result"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predictions
y_pred = lr.predict(X_test)


print(lr.score(X_test,y_test)*100)


# Evaluation
print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))

# Example Prediction
print("Prediction for [1,96,5.64,90]:", lr.predict([[1, 96, 5.64, 90]]))

# Visualization: Actual vs Predicted
plt.scatter(y_test, y_pred, color="blue", alpha=0.6)
plt.xlabel("Actual Result")
plt.ylabel("Predicted Result")
plt.title("Linear Regression - Actual vs Predicted")
plt.show()
