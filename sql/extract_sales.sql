-- Extract des ventes mensuelles
-- Auteur: Data Team
-- Dernière MAJ: 2026-02

SELECT
    date_trunc('month', order_date) as month,
    product_category,
    COUNT(*) as nb_orders,
    SUM(amount) as total_revenue
FROM orders
WHERE order_date >= :start_date
GROUP BY 1, 2
ORDER BY 1 DESC;
