SELECT name AS country, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000
ORDER BY population DESC;