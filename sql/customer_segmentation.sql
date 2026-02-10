-- Segmentation client RFM
-- Auteur: Data Team

WITH customer_metrics AS (
    SELECT
        customer_id,
        MAX(order_date) as last_order,
        COUNT(*) as frequency,
        SUM(amount) as monetary
    FROM orders
    GROUP BY customer_id
)
SELECT
    customer_id,
    NTILE(5) OVER (ORDER BY last_order) as recency_score,
    NTILE(5) OVER (ORDER BY frequency) as frequency_score,
    NTILE(5) OVER (ORDER BY monetary) as monetary_score
FROM customer_metrics;
