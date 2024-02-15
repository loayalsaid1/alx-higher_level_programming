-- list allrecords with name not null ,in descending score value
SELECT score, name
    FROM second_table
    WHERE name IS NOT NULL
    ORDER BY score DESC;
