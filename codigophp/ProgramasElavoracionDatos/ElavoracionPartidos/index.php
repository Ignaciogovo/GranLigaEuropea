<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jornadas</title>
</head>
<body>
    <?php
        include('functionClub.php');
       $n_jornada2=calculoJornada();
        $n_temporada2=calculoTemporada();
        echo "<h1>Inicio de la jornada $n_jornada2 de la temporada $n_temporada2</h1>";
    ?>
<form action="Ejecucionjornada.php" method="post">
        <input type="submit" value="inicio Jornada">
</form>

</body>
</html>