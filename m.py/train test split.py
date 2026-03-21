import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
data=pd.read_csv(r"C:\Users\SAJLE\Downloads\house prediction.csv")
print(data.head(5))
input_data=data.iloc[:,:-1]
output_data=data["Price"]
x_train,y_train,x_test,y_test=train_test_split(input_data,output_data,test_size=0.20)