<?php 

function calculoVictoria($E1,$E2,$V1,$V2){
    $final = 0;
    while($final < 1){
        //Elavoración del número aleatorio, tendrán ventaja si el valor es mayor.
        if ( $V1 < $V2){        
            $diferencia=($V2-$V1);
            if($diferencia < 6){
                $potencial2= 1.25*rand(0,10);
                $potencial1= rand(0,10);
            }elseif ($diferencia >= 6) {
                $potencial2= 1.5*rand(0,10);
                $potencial1= rand(0,10);
            }            
        }elseif( $V1 > $V2){
            $diferencia = ($V1-$V2);
            if($diferencia < 6){
                $potencial1= 1.25* rand(0,10);
                $potencial2= rand(0,10);
            }elseif ($diferencia >= 6) {
                $potencial1= 1.5* rand(0,10);
                $potencial2= rand(0,10);
            }            
        }elseif($V1 ==$V2){
            $potencial2= rand(0,10);
            $potencial1= rand(0,10);
        };
        //Asignación del equipo ganador
        if ($potencial1 < $potencial2){
            $gol1=($potencial1/2.8);
            $gol2=($potencial2/2.8);
            $gol1=round($gol1,0);
            $gol2=round($gol2,0);
            if($gol1==$gol2){
                $gol2++;
            }
            echo "gana Equipo $E2 con un $potencial2  con goles: $gol2<br>";
            echo "pierde Equipo $E1 con un $potencial1 con goles: $gol1<br>";
            $final = 1;
        }elseif ($potencial1 > $potencial2){
            $gol1=($potencial1/2.8);
            $gol2=($potencial2/2.8);
            $gol1=round($gol1,0);
            $gol2=round($gol2,0);
            if($gol1==$gol2){
                $gol1++;
            }
            echo "gana Equipo $E1 con un $potencial1 con goles: $gol1<br>";
            echo "pierde Equipo $E2 con un $potencial2 con goles: $gol2<br>";
            $final = 1;
        }
    }
}

    ?>