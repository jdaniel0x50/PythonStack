SELECT film.title AS film, CONCAT(SUBSTRING(film.description, 1, 25), "...") AS description, film.release_year, film.rating, film.special_features, category.name
FROM category
JOIN film_category ON category.category_id = film_category.category_id
JOIN film ON film_category.film_id = film.film_id
WHERE category.name = "Drama" AND film.rental_rate = 2.99
ORDER BY film.title ASC;