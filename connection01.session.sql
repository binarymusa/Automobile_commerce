
/*

USE <DB.NMAE>
DELETE FROM <table_nmae>  or filter using (DELETE FROM <table_nmae> WHERE <column.name>=<name> IN (<column_id>)
SELECT * FROM <table.name> or SELECT * FROM <table.name> WHERE <column.name>= <name>
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


--  USE Automobile;
--  UPDATE user SET username = 'shrub' WHERE id = 26;

-- SELECT * FROM importations

-- SELECT * FROM vehicles
-- UPDATE vehicles SET price = 80000 WHERE id = 30
-- SELECT * FROM vehicles WHERE 
/* UPDATE vehicles 
SET year = 
    CASE 
        WHEN id IN ('16', '17', '18', '19', '20', '21', '22', '23', '31') THEN '2024'
        WHEN id IN ('28') THEN '2021'
        WHEN id IN ('27') THEN '2022'
        WHEN id IN ('30') THEN '2023'
        ELSE car_type
    END
WHERE id IN ('30' , '31') */

-- SELECT * FROM user
-- SELECT * FROM user WHERE user_role = 1
-- UPDATE user SET user_role = 1 WHERE id = 29
DELETE FROM user WHERE id = 38

-- SELECT * FROM roles
-- SELECT * FROM roles WHERE 
-- DELETE FROM roles WHERE

-- SELECT * FROM importations
-- SELECT * FROM roles WHERE 

-- SELECT * FROM visiting_records
-- SELECT * FROM visiting_records WHERE

-- SELECT * FROM cart
-- SELECT * FROM cart WHERE  
-- DELETE FROM cart WHERE

-- SELECT * FROM purchased_items
-- SELECT * FROM purchased_items WHERE 
-- DELETE FROM purchased_items WHERE vehicle_id =

/* 
INSERT INTO importations (model, chasis_No, arrival_date, order_date)
VALUES 
(
    'Bmw','Bw05T','2024-03-04','2024-05-01'
) */
















