<?php
//include('C:/xampp/htdocs/ProyectoLiga/ProyectoLigaInventada/codigophp/ProgramasElavoracionDatos/ElavoracionPartidos/functionClub.php');


function calculotablaTemporada(){
    include("C:/xampp/htdocs/ProyectoLiga/conexion.php");
    $sentencia = $conexion->query("select max(id) from prueba_temporadas");
    $temporadas = $sentencia->fetch();
    $temporada = $temporadas[0];   //Obtencion de la temporada a partir de un array de objetos¿?
        if(empty($temporada)){
            $temporada=1;
        }
    return $temporada;
}
$temporadatabla = calculotablaTemporada();
echo $temporadatabla;
?>