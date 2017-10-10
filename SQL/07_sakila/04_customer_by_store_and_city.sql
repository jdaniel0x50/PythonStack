SELECT customer.first_name, customer.last_name, customer.email, address.address, city.city, address.postal_code
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE customer.store_id = 1 AND 
(address.city_id = 1 OR address.city_id = 42 OR address.city_id = 312 OR address.city_id = 459)
ORDER BY customer.first_name ASC;