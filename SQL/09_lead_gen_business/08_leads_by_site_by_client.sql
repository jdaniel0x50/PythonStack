SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name,
	sites.domain_name,
    COUNT(leads.leads_id) AS number_of_leads
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY clients.client_id, sites.site_id
ORDER BY clients.first_name, sites.domain_name;
