<?php
echo "<a href='index.html'>Página inicial</a><br>";
$participantes=$_POST["participantes"];
$i=0;

    //Este if no se puede usar sin javascripts
    if (isset($_POST['nombres']) && $_POST["nombres"]==1){   // Comprobación si el checkbox se ha activado.
        header("Location: lorem.php"); //Redireccionar a otra pagina
        die();
        
    }else{
        include('functionOrden.php');
        $primeros=$participantes/2;
        $array1= array(2);
        $v1=3;
        while ($v1<=$primeros){    // Ampliación array1
            array_push($array1,$v1);
            $v1++;
        }
        $array2= array($primeros+1);
        $v1=$primeros+2;
        while ($v1<=$participantes){ //Ampliación array2
            array_push($array2,$v1);
            $v1++;
        }
        planificacionjornadas($participantes,$primeros,$array1,$array2);
    }
    
?>