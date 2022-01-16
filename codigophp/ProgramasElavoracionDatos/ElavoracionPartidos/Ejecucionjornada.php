<?php
    include('functionClub.php');
        $jornada=calculoJornada();
        $n_temporada=calculoTemporada();
        $temporadatabla = calculotablaTemporada();
        if ($n_temporada != $temporadatabla){ 
            //Cada vez que se crea una nueva temporada volvemos a la jornada 1 de la temporada x, Asi lo comprobamos.
            $jornada = 1;
        }
    if ($jornada > 30){ 
        //Condicion al final de la temporada para no hacer más partidos
        echo "Debe esperar a una nueva temporada";
    }elseif ($jornada == 1 and $temporadatabla == 0){
         // Condición para la temporada 1.
        echo "<h1>Debe iniciar la temporada 1</h1>";
    }else{
         //Inicios de jornadas
        echo "Inicio Jornada";
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
       
        planificacionjornadasParaliga($jornada,$array1,$array2);
    }
    echo "<a href='index.php'>Vuelta al inicio</a>";
    if ($jornada == 30){
         //Cuando se ejecuta la ultima jornada cerramos la temporada
        $temporada = calculoTemporada();
        finalizarTemporada($temporada);
    }   
?>