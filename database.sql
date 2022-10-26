CREATE SCHEMA gatorbookdb;

CREATE TABLE gatorbookdb.user(
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    PRIMARY KEY(username)
);

INSERT INTO gatorbookdb.user(username, password) values ("root", "root");