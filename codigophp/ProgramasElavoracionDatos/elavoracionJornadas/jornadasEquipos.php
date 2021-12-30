<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calendario Equipos</title>
</head>
<body>
      <?php
        include('C:/xampp/htdocs/ProyectoLigaInventada/codigophp/CreadorJornadas/functionOrden.php');
        $array1= array(2);
        $v1=3;
        while ($v1<9){
            array_push($array1,$v1);
            $v1++;
        }
        echo "<br>";
        $array2= array(9);
        $v1=10;
        while ($v1<17){
            array_push($array2,$v1);
            $v1++;
        }
        planificacionjornadas(16,8,$array1,$array2);
    ?>
</body>
</html>