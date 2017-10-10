SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name,
    DATE_FORMAT(charged_datetime, "%Y-%m") AS billing_year_month,
    CONCAT('$', FORMAT(SUM(amount), 2)) AS total_revenue
FROM billing
LEFT JOIN clients ON billing.client_id = clients.client_id
GROUP BY clients.client_id, billing_year_month
ORDER BY clients.first_name, billing_year_month;
