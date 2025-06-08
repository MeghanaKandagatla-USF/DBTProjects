
import pandas as pd

def model(dbt, session):
    dbt.config(materialized="table", packages=["pandas"])

    sales_df = dbt.ref("sales_data").to_df()

    result = (
        sales_df
        .groupby("customer", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_amount"})
    )

    return result



