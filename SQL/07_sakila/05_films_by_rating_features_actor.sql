SELECT film.title AS film, CONCAT(SUBSTRING(film.description, 1, 25), "...") AS description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.rating = "G"
AND film.special_features LIKE "%behind the scenes%"
AND actor.actor_id = 15
ORDER BY film.title;