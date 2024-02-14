-- display same score and it number
SELECT `score`, COUNT(`score`) AS `number` FROM `second_table` GROUP BY `score`;
