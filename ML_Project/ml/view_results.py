import duckdb

conn = duckdb.connect("dbt/churn_dbt/mlproject.duckdb")

df = conn.execute("SELECT * FROM predicted_churn_by_gender").df()

print(df)
