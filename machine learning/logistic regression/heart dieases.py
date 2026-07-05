# ==============================
# 📌 Import Libraries
# ==============================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc


# ==============================
# 📌 Load Dataset
# ==============================
def load_data(path):
    data = pd.read_csv(path)
    return data


# ==============================
# 📌 Preprocessing
# ==============================
def preprocess_data(data):
    data = pd.get_dummies(data, drop_first=True)
    X = data.drop('target', axis=1)
    y = data['target']
    return X, y


# ==============================
# 📌 Train Model (Without Scaling)
# ==============================
def train_without_scaling(X_train, y_train):
    model = LogisticRegression(max_iter=1000, solver='liblinear')
    model.fit(X_train, y_train)
    return model


# ==============================
# 📌 Train Model (With Scaling)
# ==============================
def train_with_scaling(X_train, X_test, y_train):
    scaler = StandardScaler()
    
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = LogisticRegression(max_iter=1000, solver='liblinear')
    model.fit(X_train_scaled, y_train)
    
    return model, X_train_scaled, X_test_scaled


# ==============================
# 📌 Pipeline Model
# ==============================
def train_pipeline(X_train, y_train):
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(max_iter=1000))
    ])
    
    pipe.fit(X_train, y_train)
    return pipe


# ==============================
# 📌 Evaluation Function
# ==============================
def evaluate_model(y_test, y_pred):
    print("\n📊 Model Evaluation")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))


# ==============================
# 📌 Confusion Matrix Plot
# ==============================
def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()


# ==============================
# 📌 ROC Curve
# ==============================
def plot_roc_curve(model, X_test, y_test):
    y_prob = model.predict_proba(X_test)[:, 1]
    
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    
    plt.plot(fpr, tpr)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"ROC Curve (AUC = {roc_auc:.2f})")
    plt.show()


# ==============================
# 📌 Feature Importance
# ==============================
def feature_importance(model, feature_names):
    importance = pd.DataFrame({
        "Feature": feature_names,
        "Coefficient": model.coef_[0]
    })
    
    print("\n📌 Feature Importance:")
    print(importance.sort_values(by="Coefficient", ascending=False))


# ==============================
# 📌 Scatter Plot
# ==============================
def plot_scatter(data):
    plt.figure(figsize=(6,4))
    sns.scatterplot(x=data['age'], y=data['target'])
    plt.title("Age vs Heart Disease")
    plt.show()


# ==============================
# 🚀 Main Function
# ==============================
def main():
    # Load data
    data = load_data(r"C:\Users\SAJLE\Downloads\dataset\Heart  Disease.csv")
    
    # Preprocess
    X, y = preprocess_data(data)
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # ------------------------------
    # Model 1: Without Scaling
    # ------------------------------
    model_no_scale = train_without_scaling(X_train, y_train)
    y_pred_no_scale = model_no_scale.predict(X_test)
    
    print("🔹 WITHOUT SCALING")
    evaluate_model(y_test, y_pred_no_scale)
    
    # ------------------------------
    # Model 2: With Scaling
    # ------------------------------
    model_scaled, X_train_scaled, X_test_scaled = train_with_scaling(X_train, X_test, y_train)
    y_pred_scaled = model_scaled.predict(X_test_scaled)
    
    print("\n🔹 WITH SCALING")
    evaluate_model(y_test, y_pred_scaled)
    
    # ------------------------------
    # Model 3: Pipeline
    # ------------------------------
    pipe_model = train_pipeline(X_train, y_train)
    y_pred_pipe = pipe_model.predict(X_test)
    
    print("\n🔹 PIPELINE MODEL")
    evaluate_model(y_test, y_pred_pipe)
    
    # ------------------------------
    # Visualization
    # ------------------------------
    plot_confusion_matrix(y_test, y_pred_scaled)
    plot_scatter(data)
    
    # ROC Curve (use scaled model)
    plot_roc_curve(model_scaled, X_test_scaled, y_test)
    
    # Feature Importance
    feature_importance(model_scaled, X.columns)


# ==============================
# ▶ Run Project
# ==============================
if __name__ == "__main__":
    main()