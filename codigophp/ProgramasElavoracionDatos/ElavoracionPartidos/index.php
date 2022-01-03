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
        include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
        error_reporting(0); //Para eliminar los avisos de que las variables puedan estar vacias.
        $consultajornada="select jornada from prueba_partidos order by id desc";
        $n_jornada=$conexion->prepare($consultajornada, [   //Obtener datos a partir de un cursor.
            PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL,
        ]);
        $n_jornada->execute();
        $n_jornada2 =$n_jornada->jornada;
        if(!$n_jornada2){
            $n_jornada2=1;
        }
        $consultatemporada="select temporada from prueba_partidos order by id desc";
        $n_temporada=$conexion->prepare($consultatemporada, [   //Obtener datos a partir de un cursor.
            PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL,
        ]);
        $n_temporada->execute();
        $n_temporada2 =$n_temporada->temporada;
        if(!$n_temporada2){
            $n_temporada2=1;
        }
        echo "<h1>Inicio de la jornada $n_jornada2 de la temporada $n_temporada2</h1>";
        $conexion->null;
    ?>
<form action="Ejecucionjornada.php" method="post">
        <input type="submit" value="inicio Jornada">
</form>

</body>
</html>