-- Change the database encoding to (utf8mb4, collate utf8mb4_unicode_ci)
USE hbtn_0c_0
-- Change the database character setand collation
-- ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Change the character set and collation for the entire table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Change the character set and collation for a specific column <name> in the table
-- ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
