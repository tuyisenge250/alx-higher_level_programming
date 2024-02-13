-- display same score and it number
select `score`, count(`score`) as `number` from `second_table` group by `score`;
