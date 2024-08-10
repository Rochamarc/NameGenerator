SELECT  value
FROM first_names
WHERE
    value = %s AND
    gender = %s AND
    nationality = %s; 