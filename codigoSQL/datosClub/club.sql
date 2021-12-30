IF EXISTS(SELECT 1 FROM sys.tables WHERE object_id = OBJECT_ID('club'))
BEGIN;
    DROP TABLE [club];
END;
GO

CREATE TABLE [club] (
    [clubID] INTEGER NOT NULL IDENTITY(1, 1),
    [nombre] VARCHAR(255) NULL,
    [ciudad] VARCHAR(255) NULL,
    PRIMARY KEY ([clubID])
);
GO

INSERT INTO [club] (nombre,ciudad)
VALUES
  ('Los Soberanos','Barcelona'),     
  ('Club Atlético Aquiles','Salamanca'),   
  ('Unión de casados','Zaragoza'),     
  ('Olimpo Team','Sevilla'),      
  ('Kings','Madrid'),         
  ('Real Suciedad','Valencia'),
  ('Unión Penosa','Toledo'),    
  ('Don Viriato','Malaga'),         
  ('Limón F.C','Barcelona');     
INSERT INTO [club] (nombre,ciudad)
VALUES
  ('Los Plebeyos','Barcelona');   
  ('Semen Padang','Bilbao'),   
  ('War Hawks','Sevilla'),
  ('Field Warriors','Oviedo');
  ('The Gladiators','Santander'),   
  ('Llanfairpwllgwyngyll FC','Palma'),
  ('Rico Pollo','Madrid');

