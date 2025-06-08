SELECT
  gender,
  COUNT(*) AS total_customers,
  SUM(prediction) AS predicted_churns,
  ROUND(100.0 * SUM(prediction) / COUNT(*), 2) AS churn_rate_percent
FROM churn_predictions
GROUP BY gender
