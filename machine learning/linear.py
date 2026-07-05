import pandas as pd

from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from sklearn.preprocessing import StandardScaler
import joblib

data=pd.read_csv(r"C:\yash_important data\ml\house proice prediction reduce dataset.csv")

# check data shape
# print(data.shape)

# check null value
# print(data.isna())

# print(data.isnull().sum())

# print(data.columns)

X = data.drop(["price", "country"], axis=1)
y=data["price"]


# convert categorical value
X = pd.get_dummies(X, columns=["city"], drop_first=True)


X_train, X_test, y_train, y_test=train_test_split(X,y ,test_size=0.2,random_state=2)

lr=LinearRegression()
lr.fit(X_train,y_train)

# print(X.columns)

bedrooms = int(input("Bedrooms: "))
bathrooms = float(input("Bathrooms: "))
sqft_living = int(input("Sqft living: "))
sqft_lot = int(input("Sqft lot: "))
floors = int(input("Floors: "))
waterfront = int(input("Waterfront (0/1): "))
condition = int(input("Condition (1-5): "))
yr_built = int(input("Year built: "))
city = input("City (example: Seattle): ")


new_house = X.iloc[0:1].copy()
new_house = new_house.astype(float)
new_house.loc[:] = 0


new_house['bedrooms'] = bedrooms
new_house['bathrooms'] = bathrooms
new_house['sqft_living'] = sqft_living
new_house['sqft_lot'] = sqft_lot
new_house['floors'] = floors
new_house['waterfront'] = waterfront
new_house['condition'] = condition
new_house['yr_built'] = yr_built



# sab city columns 0
new_house.loc[:, new_house.columns.str.contains('city_')] = 0

# user input city ko match karo
city_col = "city_" + city

if city_col in new_house.columns:
    new_house[city_col] = 1
else:
    print("⚠️ City not found, default used")


price = lr.predict(new_house)
print("🏠 Predicted Price:", price[0])


y_pred=lr.predict(X_test)
print("Accuracy(R2 Score)",r2_score(y_test,y_pred))


scalor=StandardScaler()
X_train=scalor.fit_transform(X_train)
y_train=scalor.fit_transform(X_test)


job






# print(data.head(10))