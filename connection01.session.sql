
/*

USE <DB.NMAE>
DELETE FROM <table_nmae>  or filter using (DELETE FROM <table_nmae> WHERE <column.name>=<name> IN (<column_id>)
SELECT * FROM <table.nmae> or SELECT * FROM <table.name> WHERE <column.name>= <name>
DROP TABLE table_name;
DROP TABLE IF EXISTS table_name
INSERT INTO <table_nmae> (<column_name>) VALUES ('<valuea>'), ('v<value_b>')

-- updating a value to a column in a tabble
UPDATE <table_name> SET <column_name> = 'id_of_normal_user_role' WHERE id = <id>;
CREATE DATABASE 
ALTER TABLE vehicles DROP COLUMN a,DROP COLUMN b;

-- adding different values based on different ids

UPDATE your_table_name
SET car_type = 
    CASE 
        WHEN id IN ('a', 'b', 'c') THEN 'bmw'
        WHEN id IN ('d', 'e', 'f') THEN 'mercedes'
        WHEN id IN ('g', 'h', 'i') THEN 'rangerover'
        ELSE car_type
    END
WHERE id IN ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i');

*/

-- UPDATE user SET user_role = '1' WHERE id = 12
--  USE Automobile;

SELECT * FROM vehicles
-- SELECT * FROM user
-- SELECT * FROM cart
-- SELECT * FROM purchased_items

-- DELETE FROM cart
-- DELETE FROM purchased_items
















