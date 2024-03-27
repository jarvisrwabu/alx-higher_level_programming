-- Using LEFT JOIN to list names of cities with their atate
SELECT cities.id, cities.name, states.name
FROM cities c
LEFT JOIN states s ON c.id = s.id
ORDER BY cities.id;