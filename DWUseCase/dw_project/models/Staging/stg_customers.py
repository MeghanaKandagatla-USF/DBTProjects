import pandas as pd
def model(dbt, session):
    dbt.config(materialized="table", packages=["pandas"])
    
    ref_table = dbt.ref("customers")
    df = ref_table.to_df()
    
    return df

