-- Create a new user if not exists and grant then full priviledges 
-- over the server


-- Create the user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant PRIVILEDGES to the user
GRANT ALL ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
