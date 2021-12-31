<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jornada</title>
</head>
<body>
<?php
include('function.php');
$nombre= array("los soberanos","Club Aquiles","Olimpo","Kings","Unión Penosa","Limón F.C","semen Padang","War hawks");
$valor= array(65,47,72,50,52,35,75,71);
print_r($nombre);
echo "<br>";
$tiempo =0;
while ($tiempo < 4){
    $E1= $nombre[8-($tiempo+1)];
    $E2= $nombre[$tiempo];
    $V1= $valor[8-($tiempo+1)];
    $V2= $valor[$tiempo];
    echo "$E1($V1) VS $E2($V2)";
    echo "<br>";
    calculoVictoria($E1,$E2,$V1,$V2);
    echo "<br>";
    $tiempo++;
}
?>
</body>
</html>