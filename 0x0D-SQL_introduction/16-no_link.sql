-- lists all records of the table second_table of the database hbtn_0c_0 in a MySQL server.
-- Don’t list rows without a name value.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
