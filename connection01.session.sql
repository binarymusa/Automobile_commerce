
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

SELECT * FROM vehicles
-- SELECT * FROM vehicles WHERE  
-- UPDATE vehicles SET image_link = 'static/images/roverevoque.jpg' WHERE id = 28;

-- SELECT * FROM user
-- SELECT * FROM user WHERE user_role = 1
-- UPDATE user SET user_role = 1 WHERE id = 29

-- SELECT * FROM roles
-- SELECT * FROM roles WHERE  

-- SELECT * FROM cart
-- SELECT * FROM cart WHERE  

-- SELECT * FROM purchased_items
-- SELECT * FROM purchased_items WHERE 


-- DELETE FROM cart WHERE
-- DELETE FROM purchased_items WHERE vehicle_id = 
-- DELETE FROM user WHERE id =  31
-- DELETE FROM roles WHERE  


/* INSERT INTO vehicles (price, description, model, car_type)
VALUES 
(
    '72000',
    'Blue cabriolete, 2024 model year, 4.0L V-8 engine, 453hp',
    'Audi A8',    
    'Audi'
)
 */















