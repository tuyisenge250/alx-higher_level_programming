-- select the best how have => 10
SELECT `score`,`name` FROM
`second_table`
where `score` >= 10
ORDER BY `score` DESC;
