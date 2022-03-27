IF EXISTS(SELECT 1 FROM sys.tables WHERE object_id = OBJECT_ID('arbitros'))
BEGIN;
    DROP TABLE [arbitros];
END;
GO

CREATE TABLE [arbitros] (
    [ID] INTEGER NOT NULL IDENTITY(1, 1),
    [name] VARCHAR(255) NULL,
    [Comunidad] VARCHAR(100) NULL,
    [FechaNacimiento] date NULL,
    PRIMARY KEY ([ID])
);
GO

INSERT INTO [arbitros] (name,Comunidad,FechaNacimiento)
VALUES
  ('Juan Paula','Cantabria','1986-06-13 '),
  ('Oscar Reyes','Cantabria','1984-01-22 '),
  ('Gaspar Diaz','Andalucia','1994-09-20 '),
  ('Lukas Matias','Andalucia','1992-05-29 '),
  ('Silvestre Perez','La Rioja','1995-08-09 '),
  ('Carlos Castro','Cataluña','1984-07-06 '),
  ('Carlos Trinidad','La Rioja','1995-06-23 '),
  ('Niño Dominguez','Cantabria','1994-12-01 '),
  ('Alexander Martin','Pais Vasco','1996-11-01 '),
  ('Oscar Matias','Aragon','1996-04-13 ');
INSERT INTO [arbitros] (name,Comunidad,FechaNacimiento)
VALUES
  ('David Fuentes','Cantabria','1995-03-25 '),
  ('Maikel Soler','Madrid','1989-04-03 '),
  ('Heriberto Arias','Cantabria','1983-06-22 '),
  ('Álvaro Barbara','Pais Vasco','1988-07-12 '),
  ('Rodolfo Sanchez','Cantabria','1993-03-20 ');
