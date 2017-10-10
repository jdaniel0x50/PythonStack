SELECT film.title AS film, CONCAT(SUBSTRING(film.description, 1, 25), "...") AS description, film.release_year, film.rating, film.special_features, category.name AS genre, CONCAT_WS(" ", actor.first_name, actor.last_name) AS actor_name
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE actor.first_name = "SANDRA" AND actor.last_name = "KILMER" AND category.name = "action"
ORDER BY film.title ASC;