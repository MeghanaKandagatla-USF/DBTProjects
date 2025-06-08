import pandas as pd

def model(dbt, session):
    dbt.config(materialized="table", packages=["pandas"])

    join_Tables_df = dbt.ref("join_Tables").to_df()

    result = (
        join_Tables_df
        .groupby(["customer_id", "customer_name"], as_index=False)
        .agg(total_revenue=("order_value", "sum"))
    )

    return result
