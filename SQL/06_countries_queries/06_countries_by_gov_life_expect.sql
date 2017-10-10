SELECT name AS country, government_form, capital, life_expectancy
FROM countries
WHERE government_form LIKE "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 75
ORDER BY name ASC;
