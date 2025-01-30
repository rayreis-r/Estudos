CREATE DATABASE dogs;
USE dogs;

CREATE TABLE cachorro(
idDogs INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
raça VARCHAR(45),
pelagem VARCHAR(45)
);

CREATE TABLE tutor(
idTutor INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(45),
telefone char(11),
endereco VARCHAR(20)
);

-- Insert
INSERT INTO cachorro VALUES
(DEFAULT, 'Scott', 'Maltês', 'longa');

INSERT INTO tutor VALUES
(DEFAULT, 'Rayane', '97032-7654', 'rua cardoso');

ALTER TABLE cachorro ADD COLUMN porte VARCHAR(20);
ALTER TABLE cachorro RENAME COLUMN pelagem to pelo;

UPDATE cachorro SET porte = 'pequeno' WHERE idDogs = 1;

SELECT * FROM cachorro;
SELECT * FROM tutor;
