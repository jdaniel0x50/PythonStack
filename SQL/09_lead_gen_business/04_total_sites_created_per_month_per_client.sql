SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, DATE_FORMAT(sites.created_datetime, "%Y-%m") AS month_of_year, COUNT(sites.domain_name) AS number_sites
FROM sites
JOIN clients ON sites.client_id = clients.client_id
WHERE sites.client_id = 1
GROUP BY month_of_year
ORDER BY month_of_year;