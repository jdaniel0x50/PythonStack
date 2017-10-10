SELECT countries.name AS country, languages.language AS language, languages.percentage AS language_percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;