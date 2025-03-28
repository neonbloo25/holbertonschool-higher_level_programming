-- Creates db 'hbtn_0d_usa' and table 'cities' on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states (id),
    name VARCHAR(256) NOT NULL
);
