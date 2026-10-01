-- Query 1: Monthly revenue by category

SELECT
    month,
    category,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders
GROUP BY month, category
ORDER BY
    CASE month
        WHEN 'April' THEN 1
        WHEN 'May' THEN 2
        WHEN 'June' THEN 3
    END,
    category;

    -- Query 2: Region-wise revenue and order count

SELECT
    r.region,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_revenue,
    COUNT(*) AS order_count
FROM orders o
JOIN resellers r
    ON o.reseller_id = r.reseller_id
GROUP BY r.region
ORDER BY total_revenue DESC;

-- Query 3: Top 5 resellers by total spend

SELECT
    r.reseller_id,
    r.reseller_name,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
FROM orders o
JOIN resellers r
    ON o.reseller_id = r.reseller_id
GROUP BY r.reseller_id
HAVING total_spend > 50000
ORDER BY total_spend DESC
LIMIT 5;

-- Query 4A: Resellers who have never placed an order

SELECT
    r.reseller_id,
    r.reseller_name,
    r.region
FROM resellers r
LEFT JOIN orders o
    ON r.reseller_id = o.reseller_id
WHERE o.order_id IS NULL;

-- Query 4B: Demonstrate COUNT(*) vs COUNT(order_id)

SELECT
    r.reseller_id,
    COUNT(*) AS total_rows,
    COUNT(o.order_id) AS order_count
FROM resellers r
LEFT JOIN orders o
    ON r.reseller_id = o.reseller_id
WHERE r.reseller_id = 'RS024'
GROUP BY r.reseller_id;

-- Query 5: June AOV for Delivered orders only

SELECT
    ROUND(
        SUM(quantity * unit_price) * 1.0 / COUNT(*),
        2
    ) AS june_aov
FROM orders
WHERE month = 'June'
    AND status = 'Delivered';