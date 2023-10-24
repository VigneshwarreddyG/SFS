CREATE database IF NOT EXISTS SFS;
USE SFS;
CREATE TABLE IF NOT EXISTS accounts (
	fname VARCHAR(30),
    lname VARCHAR(30),
    address VARCHAR(200),
    username VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(80) ,
    pass VARCHAR(50),
    usertype VARCHAR(20)
);

INSERT INTO accounts (fname, lname, address, username, phone, email, pass, usertype)
SELECT 'admin',' ','admin','admin',' ',' ','admin','admin'
FROM dual
WHERE NOT EXISTS (
    SELECT 1
    FROM accounts
    WHERE username = 'admin'
);

select * from accounts;




