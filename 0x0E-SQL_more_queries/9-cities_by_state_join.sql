-- Using INNER JOIN to list names of cities with their atate (COmmon values in both tables)
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id;