SET SQL_SAFE_UPDATES = 0;
INSERT INTO friendships
(user_id, friend_id, created_at, updated_at)
VALUES
(1, 4, current_timestamp(), current_timestamp()),
(1, 3, current_timestamp(), current_timestamp()),
(1, 2, current_timestamp(), current_timestamp()),
(2, 1, current_timestamp(), current_timestamp()),
(3, 1, current_timestamp(), current_timestamp()),
(4, 1, current_timestamp(), current_timestamp());