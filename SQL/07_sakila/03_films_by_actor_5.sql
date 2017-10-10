SELECT actor.actor_id, actor.first_name, actor.last_name, film.title AS film, film.description, film.release_year
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5
ORDER BY film.release_year DESC;