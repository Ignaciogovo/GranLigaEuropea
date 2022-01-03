CREATE TABLE historicoClub(
    [id] int NOT NULL IDENTITY(1, 1) PRIMARY KEY,
    id_club int not null,
    nJugadores int,
    nExtranjeros int,
    valorTotal varchar(100),
	fechamodificacion datetime not null,
    CONSTRAINT [FK_historicoclub.id_club] FOREIGN KEY (id_club) REFERENCES club([id])
)