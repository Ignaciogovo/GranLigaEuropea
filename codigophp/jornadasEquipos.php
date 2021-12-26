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
        $array1= array(2);
        $v1=3;
        while ($v1<9){
            array_push($array1,$v1);
            $v1++;
        }
        print_r($array1);
        echo "<br>";
        $array2= array(9);
        $v1=10;
        while ($v1<17){
            array_push($array2,$v1);
            $v1++;
        }
        $tiempo = 1;
        while ($tiempo <17){
            echo " Jornada $tiempo <br>";
            if ($tiempo == 8){
                echo " Comienzo de la mitad de la temporada<br>";
            }
            $v2 = 0;
            echo 1 . " vs " . $array2[$v2];
            echo "<br>";
            while ( $v2 < 7){ 
            echo $array1[$v2] . " vs " . $array2[$v2+1];
            echo "<br>";
            $v2++;
        }
        echo "<br>";
        $last = array_pop($array1);
        $first = array_shift($array2);
            array_unshift($array1, $first);
            array_push($array2,$last);
            //print_r($array1);
            echo "<br>";
            $tiempo ++;
        }
    ?>
</body>
</html>