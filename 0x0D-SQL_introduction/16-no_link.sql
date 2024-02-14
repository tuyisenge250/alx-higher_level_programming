-- display all data within table and it values
-- if name not null
SELECT `score`, `name` FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
