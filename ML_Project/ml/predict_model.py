import duckdb
import pandas as pd
import joblib
import os

# 1. Load trained model
model = joblib.load("models/model.pkl")

# 2. Load features from DuckDB
conn = duckdb.connect("../dbt/churn_dbt/mlproject.duckdb")
df = conn.execute("SELECT * FROM customer_features").df()
X = df.drop(columns=["customerID", "label"])
X = pd.get_dummies(X)

# Match columns with training (for safety in real cases you'd store columns)
# 3. Make predictions
df["prediction"] = model.predict(X)

# 4. Save predictions to DuckDB
conn.execute("DROP TABLE IF EXISTS churn_predictions")
conn.execute("CREATE TABLE churn_predictions AS SELECT * FROM df")

print("✅ Predictions saved to churn_predictions table in dbt/churn_dbt/mlproject.duckdb")
