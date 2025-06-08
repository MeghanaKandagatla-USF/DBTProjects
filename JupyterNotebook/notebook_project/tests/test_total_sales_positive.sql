
-- Fail if any total_amount is less than or equal to 0
SELECT *
FROM {{ ref('total_sales') }}
WHERE total_amount <= 0
