-- Column id has 2 constraints
CREATE TABLE IF NOT EXISTS unique_id
(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);