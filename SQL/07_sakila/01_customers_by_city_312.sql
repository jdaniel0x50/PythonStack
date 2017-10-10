use sakila;
SELECT customer.first_name, customer.last_name, customer.email, address.address, address.city_id, city.city, address.postal_code
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE address.city_id = 312;