-- Create a DATABSE
-- And table if not exists with unique  id AS PRIMARY KEY and name

-- Create the databse
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table into the database
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id)
);
