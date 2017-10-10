SELECT film.film_id, film.title AS film, actor.actor_id, CONCAT_WS(" ", actor.first_name, actor.last_name) AS actor
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369
ORDER BY actor;
