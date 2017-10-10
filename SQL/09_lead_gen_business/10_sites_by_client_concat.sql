SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name,
    GROUP_CONCAT(sites.domain_name, ",  ") AS sites_owned
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id
ORDER BY clients.first_name, sites.domain_name;
