SELECT countries.name AS country, cities.name AS city, cities.population AS population
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = "Mexico" AND cities.population > 500000
ORDER BY population DESC;