CREATE DATABASE tutorial_db;
USE tutorial_db;

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(100),
    price INT
);