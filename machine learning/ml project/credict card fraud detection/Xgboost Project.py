import pandas as pd
from sklearn.preprocessing import StandardScaler

data=pd.read_csv(r"C:\Users\SAJLE\Downloads\ml project\dataset credit card.csv")

x=data.drop("Class",axis=1)
y=data["Class"]

# train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)



# i check class is imbalenced
# print(data["Class"].value_counts())
# Class
# 0    284315
# 1       492
scalor=StandardScaler()
# So we smote for balance this data
from imblearn.over_sampling import SMOTE
smote=SMOTE(random_state=42)
X_train,y_train=smote.fit_resample(X_train,y_train)
scalor.fit_transform(X_train)

# print(y_train.value_counts())
# Class
# 0    227451
# 1    227451


# Feature scaling krna h 

scalor=StandardScaler()
X_train=scalor.fit_transform(X_train)
X_test=scalor.transform(X_test)









# import xgboost first
from xgboost import XGBClassifier

model=XGBClassifier(n_estimators=100,max_depth=6,learning_rate=0.1,random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)


# Thresold 
y_prob = model.predict_proba(X_test)[:,1]
y_pred=(y_prob > 0.7).astype(int)


# Evaluation
from sklearn.metrics import accuracy_score,classification_report
# print("Accuracy score:",accuracy_score(y_test,y_pred))
# print("Classification Report:",classification_report(y_test,y_pred))






# Roc curve
from sklearn.metrics import roc_curve,roc_auc_score
import matplotlib.pyplot as plt

fpr,tpr,_=roc_curve(y_test,y_prob)

plt.plot(fpr,tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
# plt.show()


# Feature importance
import matplotlib.pyplot as plt

importance = model.feature_importances_
plt.bar(range(len(importance)), importance)
plt.title("Feature Importance")
# plt.show()


# auc score
# print("Auc score:",roc_auc_score(y_test,y_prob))





import pickle
pickle.dump(model,open("xgb_model.pkl","wb"))
pickle.dump(scalor,open("xgb_scaler.pkl","wb"))

print("✅ Model & Scaler saved successfully!")


import pandas as pd
import pickle

# ==============================
# LOAD MODEL + SCALER
# ==============================
model = pickle.load(open("xgb_model.pkl", "rb"))
scaler = pickle.load(open("xgb_scaler.pkl", "rb"))

THRESHOLD = 0.7

# ==============================
# PREDICT FUNCTION
# ==============================
def predict_file(file_path):

    try:
        # Load user file
        df = pd.read_csv(file_path)
        if "Class" in df.columns:
            df = df.drop("Class", axis=1)

        # 🔴 IMPORTANT CHECK
        required_cols = list(x.columns)

        if list(df.columns) != list(required_cols):
            print("❌ Column mismatch!")
            print("Expected:", required_cols)
            print("Got:", list(df.columns))
            return

        # Scale
        df_scaled = scaler.transform(df)

        # Predict
        probs = model.predict_proba(df_scaled)[:, 1]
        preds = (probs > THRESHOLD).astype(int)

        # Add results
        df["Fraud_Prob"] = probs
        df["Prediction"] = preds

        # Save output
        df.to_csv("prediction_output.csv", index=False)

        print("\n✅ Prediction Completed!")
        print(df.head())

    except Exception as e:
        print("❌ Error:", str(e))


file_path = input("Enter CSV file path: ")

predict_file(file_path)

print("\n📊 Summary:")
print("Total Transactions:", len(df))
print("Fraud Detected:", df["Prediction"].sum())
print("Fraud %:", round(df["Prediction"].mean()*100, 2), "%")