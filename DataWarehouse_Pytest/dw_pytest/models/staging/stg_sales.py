def model(dbt, session):
    dbt.config(materialized="table", packages=["pandas"])

    df = dbt.ref("sales_data").to_df()

    df = df.rename(columns={
        "Order ID": "order_id",
        "Customer Name": "customer_name",
        "Sales Amount": "sales_amount"
    })

    return df
