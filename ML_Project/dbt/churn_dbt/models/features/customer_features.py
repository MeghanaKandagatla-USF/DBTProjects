import pandas as pd

def model(dbt, session):
    dbt.config(
        materialized="table",
        packages=["pandas"]
    )

    df = dbt.ref("churn_data").to_df()

    # Create features and clean data
    df["label"] = df["Churn"].apply(lambda x: 1 if x == "Yes" else 0)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    selected_cols = [
        "customerID", "gender", "SeniorCitizen", "Partner", "Dependents",
        "tenure", "MonthlyCharges", "TotalCharges", "label"
    ]

    return df[selected_cols]
