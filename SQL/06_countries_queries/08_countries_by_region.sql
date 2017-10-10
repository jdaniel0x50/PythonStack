SELECT countries.region AS Region, COUNT(countries.name) AS num_countries
FROM countries
GROUP BY countries.region
ORDER BY num_countries DESC;