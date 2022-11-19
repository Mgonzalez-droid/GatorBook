CREATE SCHEMA gatorbookdb;

CREATE TABLE gatorbookdb.user(
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    PRIMARY KEY(username)
);

INSERT INTO gatorbookdb.user(username, password) values ("root", "password");
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
flush privileges;

/*Gatorbook groups */

USE gatorbookdb;

/*
CREATE TABLE groupListing (
	Memberid int NOT NULL AUTO_INCREMENT,
	GroupName VARCHAR(255),
	PRIMARY KEY (Memberid)
);
*/