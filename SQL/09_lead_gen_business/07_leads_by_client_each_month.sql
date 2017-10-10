SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name,
	DATE_FORMAT(sites.created_datetime, "%Y-%m") AS month_of_year, 
	COUNT(leads.leads_id) AS number_of_leads
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE DATE_FORMAT(sites.created_datetime, "%Y") = 2011
	AND DATE_FORMAT(sites.created_datetime, "%m") >= 1
	AND DATE_FORMAT(sites.created_datetime, "%m") <= 6
GROUP BY clients.client_id, month_of_year
ORDER BY clients.first_name, month_of_year;
