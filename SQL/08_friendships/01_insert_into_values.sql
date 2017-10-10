use mydb;
SET SQL_SAFE_UPDATES = 0;
INSERT INTO users
(first_name, last_name, created_at, updated_at)
VALUES
("Chris", "Baker", current_timestamp(), current_timestamp()),
("Diana", "Smith", current_timestamp(), current_timestamp()),
("James", "Johnson", current_timestamp(), current_timestamp()),
("Jessica", "Davidson", current_timestamp(), current_timestamp());