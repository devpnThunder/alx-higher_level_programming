-- A script that lists all records with a score >= 10 in a table in a database in MySQL server
SELECT `score`, `name` FROM `second_name` WHERE `score` >= 10 ORDER BY `score` DESC;
