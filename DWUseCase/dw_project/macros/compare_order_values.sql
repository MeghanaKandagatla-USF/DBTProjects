{% macro compare_order_values(args) %}
import pandas as pd

def test(model_df, ref, session):
    raw_df = ref('{{ args.other_table }}').toPandas()
    
    merged = pd.merge(model_df.toPandas(), raw_df, on="order_id", suffixes=('_actual', '_expected'))

    mismatches = merged[merged["order_value_actual"] != merged["order_value_expected"]]

    return mismatches
{% endmacro %}
