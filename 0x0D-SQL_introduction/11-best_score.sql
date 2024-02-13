-- select the best how have => 10
select `score`,`name` from
`second_table`
where `score` >= 10
ORDER BY `score` DESC;
