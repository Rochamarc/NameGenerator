ALTER DATABASE NameGeneratorDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE first_names(
    id INT PRIMARY KEY AUTO_INCREMENT,
    value VARCHAR(200) NOT NULL,
    gender CHAR(1) NOT NULL,
    nationality VARCHAR(100)
);

CREATE TABLE last_names(
    id INT PRIMARY KEY AUTO_INCREMENT,
    value VARCHAR(200) NOT NULL,
    nationality VARCHAR(100)
);


ALTER TABLE `first_names` ADD UNIQUE `first_name_uniqueness`(`value`, `gender`, `nationality`);
ALTER TABLE `last_names` ADD UNIQUE `last_name_uniqueness`(`value`, `nationality`);

DELIMITER $

-- Alter this to include gender
CREATE FUNCTION GET_FULL_NAME(FIRST_NAME_NATIONALITY VARCHAR(200), LAST_NAME_NATIONALITY VARCHAR(100))
RETURNS VARCHAR(400) 
DETERMINISTIC
BEGIN
	DECLARE first_name VARCHAR(200);
	DECLARE last_name VARCHAR(200);

    SELECT first_names.value        
    FROM first_names
        WHERE first_names.nationality = FIRST_NAME_NATIONALITY 
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


DELIMITER ;