-- display all data within table and it values
-- if name not null
select `score`, `name` from `second_table`
where `name` != ""
order by `score` desc;
