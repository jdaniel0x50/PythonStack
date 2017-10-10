SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, sites.domain_name AS sites_owned
FROM sites
JOIN clients ON sites.client_id = clients.client_id
WHERE sites.client_id = 10;

