-- Creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Give all privileges on your MySQL server to the user `user_0d_1`
GRANT ALL PRIVILEGES 
    ON *.*
    TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
