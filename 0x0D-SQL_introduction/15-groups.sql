-- A script that lists the number of records with the same score in the table of a database in MySQL server
SELECT COUNT(`score`) AS `number` FROM `second_table` ORDER BY`number` ASC;
