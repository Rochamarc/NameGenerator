ALTER DATABASE NameGeneratorDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE first_names(
    id INT PRIMARY KEY AUTO_INCREMENT,
    value VARCHAR(200) NOT NULL,
    gender CHAR(1) NOT NULL,
    nationality VARCHAR(100) NOT NULL
);

CREATE TABLE last_names(
    id INT PRIMARY KEY AUTO_INCREMENT,
    value VARCHAR(200) NOT NULL,
    nationality VARCHAR(100) NOT NULL
);


ALTER TABLE `first_names` ADD UNIQUE `first_name_uniqueness`(`value`, `gender`, `nationality`);
ALTER TABLE `last_names` ADD UNIQUE `last_name_uniqueness`(`value`, `nationality`);

ALTER TABLE first_names CHANGE `value` `value` VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE last_names CHANGE `value` `value` VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

DELIMITER $

CREATE FUNCTION GET_FULL_NAME(FIRST_NAME_NATIONALITY VARCHAR(200), LAST_NAME_NATIONALITY VARCHAR(100), GENDER CHAR(1))
RETURNS VARCHAR(400) 
DETERMINISTIC
BEGIN
	DECLARE first_name VARCHAR(200);
	DECLARE last_name VARCHAR(200);

    SELECT first_names.value        
    FROM first_names
        WHERE first_names.nationality = FIRST_NAME_NATIONALITY AND first_names.gender = GENDER
        ORDER BY RAND() LIMIT 1
    INTO first_name;
	
    SELECT last_names.value
    FROM last_names
        WHERE last_names.nationality = LAST_NAME_NATIONALITY
        ORDER BY RAND() LIMIT 1
    INTO last_name;
   	
    RETURN CONCAT(first_name, ' ', last_name);
END;
$

CREATE FUNCTION GET_FULL_ASIAN_NAME(NATIONALITY VARCHAR(200), GENDER CHAR(1))
RETURNS VARCHAR(400)
DETERMINISTIC
BEGIN
    DECLARE first_name VARCHAR(200);
    DECLARE last_name VARCHAR(200);

    SELECT first_name.value 
    FROM first_names
        WHERE first_names.nationality = NATIONALITY AND first_names.gender = GENDER
        ORDER BY RAND() LIMIT 1
    INTO first_name;

    SELECT last_name.value 
    FROM last_names
        WHERE last_names.nationality = NATIONALITY
        ORDER BY RAND() LIMIT 1
    INTO last_name;

    RETURN CONCAT(last_name, ' ', first_name);
END;


-- CREATE FUNCTION GET_FULL_RANDOM_NAME()
-- RETURNS VARCHAR(400)
-- DETERMINISTIC
-- BEGIN
--     DECLARE first_name VARCHAR(200);
--     DECLARE last_name VARCHAR(200);
--     DECLARE nationality VARCHAR(100);
--     DECLARE full_name VARCHAR(400);

--     SELECT nationality 
--     FROM last_names 
--         GROUP BY nationality 
--         ORDER BY RAND() LIMIT 1 
--     INTO nationality;

--     SELECT fn.value
--         FROM first_names fn
--         WHERE fn.nationality = nationality
--         ORDER BY RAND() LIMIT 1
--     INTO first_name;

--     SELECT ln.value
--         FROM last_names ln 
--         WHERE ln.nationality = nationality 
--         ORDER BY RAND() LIMIT 1
--     INTO last_name;

--     IF nationality IN ('Korean', 'Japanese', 'Chinese', 'Vietnamese') 
--     THEN SET full_name = CONCAT(last_name, ' ', first_name);
--     ELSE SET full_name = CONCAT(first_name, ' ', last_name);
--     END IF;
        
--     RETURN full_name;
-- END;
$

DELIMITER ;