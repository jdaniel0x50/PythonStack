SELECT countries.name AS "Country Name", cities.name AS "City Name", cities.district AS District, cities.population AS Population
FROM countries
LEFT JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = "Argentina" AND
cities.district = "Buenos Aires" AND
cities.population > 500000
ORDER BY cities.name ASC;
