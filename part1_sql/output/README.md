
# Part 1 SQL Output

This folder contains the CSV files generated from the SQL queries in the Meesho Reseller Operations Capstone Project.

## Output Files

1. `monthly_category_revenue.csv` – Monthly revenue and order count by category.
2. `region_revenue.csv` – Total revenue and order count by region.
3. `top_resellers.csv` – Top 5 resellers with total spending above INR 50,000.
4. `inactive_resellers.csv` – Resellers who have never placed an order.
5. `left_join_count_demo.csv` – Demonstration of COUNT(*) and COUNT(order_id).
6. `june_delivered_aov.csv` – Average order value for June delivered orders.

## LEFT JOIN Count Demonstration

Reseller RS024 (Ahmedabad Reseller 6) has never placed an order.

When we use a LEFT JOIN, SQL keeps the reseller row even when there is no matching order.

For RS024:
- COUNT(*) = 1
- COUNT(order_id) = 0

COUNT(*) counts the unmatched row created by the LEFT JOIN.
COUNT(order_id) ignores NULL values, so it returns 0.

Therefore, COUNT(*) cannot be used to identify resellers with zero matching orders. COUNT(order_id) is the correct choice for this demonstration.