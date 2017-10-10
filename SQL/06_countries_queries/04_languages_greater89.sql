SELECT countries.name AS country, languages.language AS language, languages.percentage AS percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;