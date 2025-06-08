import duckdb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import os

# 1. Connect to DuckDB and load feature data
conn = duckdb.connect("../dbt/churn_dbt/mlproject.duckdb")
df = conn.execute("SELECT * FROM customer_features").df()

# 2. Basic preprocessing
X = df.drop(columns=["customerID", "label"])
X = pd.get_dummies(X)  # one-hot encoding for categoricals
y = df["label"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)

# 6. Save model and output
os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

joblib.dump(model, "models/model.pkl")

with open("outputs/evaluation.txt", "w") as f:
    f.write(report)

print("✅ Model trained and saved to models/model.pkl")
print("📊 Evaluation report saved to outputs/evaluation.txt")

conn.close()