-- Create a database and a user with SELECT priviledge to it.


-- Create the databse.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant select privilidge to the user on database
GRANT SELECT ON hbtn_0d_2.* to 'user_0d_2'@'localhost';
