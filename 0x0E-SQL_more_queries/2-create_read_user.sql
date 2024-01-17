-- Creates the database hbtn_0d_2 and the user user_0d_2.

-- Create new database `hbtn_0d_2`
CREATE DATABASE 
    IF NOT EXISTS `hbtn_0d_2`;

-- Creates the MySQL server user user_0d_2
CREATE USER 
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';

-- Give all privileges on your MySQL server to the user `user_0d_2`
GRANT SELECT 
    ON `hbtn_0d_2`.*
    TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
