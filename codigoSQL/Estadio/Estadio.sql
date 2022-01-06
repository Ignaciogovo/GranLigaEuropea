IF EXISTS(SELECT 1 FROM sys.tables WHERE object_id = OBJECT_ID('clasificacion'))
BEGIN;
    DROP TABLE [clasificacion];
END;
GO

CREATE TABLE [estadios] (
    [nombre] VARCHAR(255) NULL,
    [id_club] INTEGER PRIMARY KEY,
    [capacidad] INTEGER NULL
);
GO
    ALTER TABLE ESTADIOS  ADD CONSTRAINT [FK_estadios.id_club]
    FOREIGN KEY ([id_club])
    REFERENCES [club]([id])
    
INSERT INTO [estadios] (nombre,id_club,capacidad)
VALUES
  ('Estadio de  la Luz',1,35554),
  ('Ernst Happel Park',4,66739),
  ('El Estadio Azul',3,31997),
  ('Croqueta Park',2,19417),
  ('Estadio Pensativo',6,38006),
  ('Estadio Deportivo Espiral',5,68000),
  ('HDI-Arena',7,25299),
  ('El Monumental',8,31100),
  ('Estadio de los Pajaritos',9,25367),
  ('Camp Siu',10,73620);
  
INSERT INTO [estadios] (nombre,id_club,capacidad)
VALUES
  ('San Marcos',11,48437),
  ('El Campín',12,28993),
  ('Olímpico de Oviedo ',13,33605),
  ('Estadio-Coliseo la guardia',14,40455),
  ('La Olla',15,29232),
  ('El Cementerio',16,39029);
  
