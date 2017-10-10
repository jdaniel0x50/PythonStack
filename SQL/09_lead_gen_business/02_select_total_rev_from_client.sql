SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, CONCAT('$', FORMAT(SUM(amount), 2)) AS total_revenue
FROM billing
JOIN clients ON billing.client_id = clients.client_id
WHERE billing.client_id = 2
GROUP BY billing.client_id;
