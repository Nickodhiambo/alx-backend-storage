-- A file that creates a table with three fields

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
	)
