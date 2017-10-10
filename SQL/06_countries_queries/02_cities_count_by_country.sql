SELECT countries.name AS country, COUNT(cities.id) AS count_cities
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY count_cities DESC;