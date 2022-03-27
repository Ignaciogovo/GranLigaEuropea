CREATE TABLE historicoJugadores (
  [id] int NOT NULL IDENTITY(1, 1) PRIMARY KEY,
  id_jugadores int not NULL,
  id_club int not NULL,
  valor varchar(100),
  fechamodificacion DATETIME not NULL,
  CONSTRAINT [FK_historicojugadores.id_club] FOREIGN KEY (id_club) REFERENCES club([id]),
  CONSTRAINT [FK_historicojugadores.id_jugadores] FOREIGN KEY (id_jugadores) REFERENCES jugadores([id])
)