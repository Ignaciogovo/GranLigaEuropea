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
       $n_jornada=calculoJornada();
        $n_temporada=calculoTemporada();
        if($n_jornada > 30){
            echo "<h1>Final de la temporada $n_temporada</h1>";
        }elseif ($n_jornada = 30) {
            echo "<h1>Jornada 30, la ultima jornada de la temporada $n_temporada</h1>";
        }else {
            echo "<h1>Inicio de la jornada $n_jornada de la temporada $n_temporada</h1>";
        }
    ?>
<form action="Ejecucionjornada.php" method="post">
        <input type="submit" value="inicio Jornada">
</form>
<br>
<form action="CreacionTemporada.php" method="post">
        <input type="submit" value="Iniciar Nueva temporada">
</form>

</body>
</html>