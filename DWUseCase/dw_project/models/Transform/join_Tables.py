import pandas as pd

def model(dbt, session):
    dbt.config(materialized="table", packages=["pandas"])

    orders_df = dbt.ref("stg_orders").to_df()
    products_df = dbt.ref("stg_products").to_df()
    customers_df = dbt.ref("stg_customers").to_df()

    merged_df = orders_df.merge(customers_df, on="customer_id", how="left")
    merged_df = merged_df.merge(products_df, on="product_id", how="left")
    
    merged_df["order_value"] = merged_df["quantity"] * merged_df["price"]

    return merged_df
