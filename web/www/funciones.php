<?php
function clasificacion(){
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "select * from clasificacionview";

  if ($resultados = mysqli_query($conexion,$consulta))
  {
    // Fetch one and one row
    while ($row=mysqli_fetch_row($resultados))
      {
        echo "<tr>";
        echo "<th scope='col'>".$row[0]."</th>";
        echo " <td>".$row[1]." </td> ";
        echo " <td>".$row[2]." </td> ";
        echo " <td>".$row[3]." </td> ";
        echo " <td>".$row[4]." </td> ";
        echo " <td>".$row[5]." </td> ";
        echo " <td>".$row[6]." </td> ";
        echo " <td>".$row[7]." </td> ";
        echo " <td>".$row[8]." </td> ";
        echo "</tr>";
      }
      //end while
    // Free result set
    mysqli_free_result($resultados);
  }// end if
};

function EstadisticasTotales(){
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "select nombre, goles, asistencias, amarillas, rojas,
  VecesTitular,partidosTotales,posicion,
  case when valor >1000000 then concat(round((valor / 1000000),2),'M')
    when valor <1000000 then concat(round((valor / 1000),2),'K')
    when valor =1000000 then '1M'
    end as valor,
    club
    from estadisticas_totales
	limit 20 ";

  if ($resultados = mysqli_query($conexion,$consulta))
  {
    $sumador = 1;
    // Fetch one and one row
    while ($row=mysqli_fetch_row($resultados))
      {
        echo "<tr>";
        echo "<th scope='col'>".$sumador."</th>";
        echo " <td>".$row[0]." </td> ";
        echo " <td>".$row[1]." </td> ";
        echo " <td>".$row[2]." </td> ";
        echo " <td>".$row[3]." </td> ";
        echo " <td>".$row[4]." </td> ";
        echo " <td>".$row[5]." </td> ";
        echo " <td>".$row[6]." </td> ";
        echo " <td>".$row[7]." </td> ";
        echo " <td>".$row[8]." </td> ";
        echo " <td>".$row[9]." </td> ";
        echo "</tr>";
        $sumador++;
      }
      //end while
    // Free result set
    mysqli_free_result($resultados);
  }// end if
}
function maximosAsistentes(){
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "select nombre, asistencias, asistencias/partidosTotales as porcentajeAsistencias,
    partidosTotales,
    case when valor >1000000 then concat(round((valor / 1000000),2),'M')
    when valor <1000000 then concat(round((valor / 1000),2),'K')
    when valor =1000000 then '1M'
    end as valor,club
    from estadisticas_totales
    order by asistencias desc
	limit 20 ";

  if ($resultados = mysqli_query($conexion,$consulta))
  {
    $sumador = 1;
    // Fetch one and one row
    while ($row=mysqli_fetch_row($resultados))
      {
        echo "<tr>";
        echo "<th scope='col'>".$sumador."</th>";
        echo " <td>".$row[0]." </td> ";
        echo " <td>".$row[1]." </td> ";
        echo " <td>".$row[2]." </td> ";
        echo " <td>".$row[3]." </td> ";
        echo " <td>".$row[4]." </td> ";
        echo " <td>".$row[5]." </td> ";
        echo "</tr>";
        $sumador++;
      }
      //end while
    // Free result set
    mysqli_free_result($resultados);
  }// end if
};
function maximosGoleadores(){
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "select nombre, goles, goles/partidosTotales as porcentajeGoles,
    partidosTotales,
    case when valor >1000000 then concat(round((valor / 1000000),2),'M')
    when valor <1000000 then concat(round((valor / 1000),2),'K')
    when valor =1000000 then '1M'
    end as valor,club
    from estadisticas_totales
	limit 20 ";

  if ($resultados = mysqli_query($conexion,$consulta))
  {
    $sumador = 1;
    // Fetch one and one row
    while ($row=mysqli_fetch_row($resultados))
      {
        echo "<tr>";
        echo "<th scope='col'>".$sumador."</th>";
        echo " <td>".$row[0]." </td> ";
        echo " <td>".$row[1]." </td> ";
        echo " <td>".$row[2]." </td> ";
        echo " <td>".$row[3]." </td> ";
        echo " <td>".$row[4]." </td> ";
        echo " <td>".$row[5]." </td> ";
        echo "</tr>";
        $sumador++;
      }
      //end while
    // Free result set
    mysqli_free_result($resultados);
  }// end if
}
function maximosparticipantes(){
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "select nombre, (goles+asistencias)as participaciones,goles, asistencias,
    partidosTotales, posicion,
    case when valor >1000000 then concat(round((valor / 1000000),2),'M')
    when valor <1000000 then concat(round((valor / 1000),2),'K')
    when valor =1000000 then '1M'
    end as valor,club
    from estadisticas_totales
    order by participaciones desc
	limit 20 ";

  if ($resultados = mysqli_query($conexion,$consulta))
  {
    $sumador = 1;
    // Fetch one and one row
    while ($row=mysqli_fetch_row($resultados))
      {
        echo "<tr>";
        echo "<th scope='col'>".$sumador."</th>";
        echo " <td>".$row[0]." </td> ";
        echo " <td>".$row[1]." </td> ";
        echo " <td>".$row[2]." </td> ";
        echo " <td>".$row[3]." </td> ";
        echo " <td>".$row[4]." </td> ";
        echo " <td>".$row[5]." </td> ";
        echo " <td>".$row[6]." </td> ";
        echo " <td>".$row[7]." </td> ";
        echo "</tr>";
        $sumador++;
      }
      //end while
    // Free result set
    mysqli_free_result($resultados);
  }// end if
}
function maximosTarjetas(){
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "select nombre,amarillas+rojas total,amarillas,rojas,partidosTotales,posicion,
    case when valor >1000000 then concat(round((valor / 1000000),2),'M')
    when valor <1000000 then concat(round((valor / 1000),2),'K')
    when valor =1000000 then '1M'
    end as valor,club
    from estadisticas_totales
    order by total desc, rojas desc, amarillas desc
	limit 20 ";

  if ($resultados = mysqli_query($conexion,$consulta))
  {
    $sumador = 1;
    // Fetch one and one row
    while ($row=mysqli_fetch_row($resultados))
      {
        echo "<tr>";
        echo "<th scope='col'>".$sumador."</th>";
        echo " <td>".$row[0]." </td> ";
        echo " <td>".$row[1]." </td> ";
        echo " <td>".$row[2]." </td> ";
        echo " <td>".$row[3]." </td> ";
        echo " <td>".$row[4]." </td> ";
        echo " <td>".$row[5]." </td> ";
        echo " <td>".$row[6]." </td> ";
        echo " <td>".$row[7]." </td> ";
        echo "</tr>";
        $sumador++;
      }
      //end while
    // Free result set
    mysqli_free_result($resultados);
  }// end if
}

function selectJornada(){
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "select jornada from partidos where temporada = (select max(id) from temporada) order by jornada desc;";
  if ($jornada = mysqli_query($conexion,$consulta))
  {
    // Fetch one and one row
  $jornada=mysqli_fetch_row($jornada);
  $jornada = $jornada[0];
  return($jornada);
  }
  
}
function selectTemporada(){
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = " select max(id) from temporada;";
  if ($temporada= mysqli_query($conexion,$consulta))
  {
    // Fetch one and one row
  $temporada=mysqli_fetch_row($temporada);
  $temporada = $temporada[0];
  return($temporada);
  }
  
}






function selectGoles($local,$visitante){
  require_once("conexion.php");
  $conexion = conexion();
  $consulta = "select goles_local,goles_visitante from partidos where temporada = (select max(id) from temporada) and id_local =$local and id_visitante=$visitante;";
  
  if ($resultados = mysqli_query($conexion,$consulta))
  {
    // Fetch one and one row
  $row=mysqli_fetch_row($resultados);
  mysqli_free_result($resultados);
  $golLocal = $row[0];
  $golvisitante = $row[1];
  $goles = [$golLocal,$golvisitante];
  return($goles);
  }
}
function SelectNombreClub($id_club){
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "select nombre from club where id = $id_club;";
  if ($resultados = mysqli_query($conexion,$consulta))
  {
    // Fetch one and one row
  $nombre_club=mysqli_fetch_row($resultados);
  $nombre_club= $nombre_club[0];
  return($nombre_club);
  }
}

function select_calendario($jornada,$temporada)
{
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "select id_local,(select nombre from club where id=id_local) local_,id_visitante,(select nombre from club where id= id_visitante) visitante from liga.calendario where temporada = $temporada and jornada = $jornada ";

  if ($resultados = mysqli_query($conexion,$consulta))
    {
      $calendario_array=array();
      // Fetch one and one row
      while ($row=mysqli_fetch_row($resultados))
        {
          $jornada_array=array(
            'temporada'=>$temporada,
            'jornada'=>$jornada,
            'id_local'=>$row[0],
            'local'=>$row[1],
            'id_visitante'=>$row[2],
            'visitante'=>$row[3]
          );
        $calendario_array[]=$jornada_array;
        }
        //end while
      // Free result set
      mysqli_free_result($resultados);
    }// end if
    else{
      $calendario_array=FALSE;
    }
    return($calendario_array);
}

function select_control_partidos($jornada,$temporada)
{
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "select 1 from liga.partido where temporada = $temporada and jornada = $jornada ";

  if ($resultado = mysqli_query($conexion,$consulta))
    {
      $resultado=true;
    }// end if
    else{
      $resultado=false;
    }
    return($resultado);
}

function select_partidos($jornada,$temporada)
{
  include_once("conexion.php");
  $conexion = conexion();
  $consulta = "SELECT id_local,(select nombre from club where id=id_local) local_,id_visitante,(select nombre from club where id= id_visitante) visitante,goles_local,goles_visitante,id_arbitro,(select nombre from arbitros where id=id_arbitro) arbitro, replace(aforo,'%','') aforo FROM liga.partidos where temporada = $temporada and jornada = $jornada ";

  if ($resultado = mysqli_query($conexion,$consulta))
    {
      $partidos_array=array();
      // Fetch one and one row
      while ($row=mysqli_fetch_row($resultado))
        {
          $jornada_array=array(
            'temporada'=>$temporada,
            'jornada'=>$jornada,
            'id_local'=>$row[0],
            'local'=>$row[1],
            'id_visitante'=>$row[2],
            'visitante'=>$row[3],
            'goles_local'=>$row[4],
            'goles_visitante'=>$row[5],
            'id_arbitro'=>$row[6],
            'arbitro'=>$row[7],
            'aforo'=> $row[8]
          );
        $partidos_array[]=$jornada_array;
        }
   }// end if
    else{
      $partidos_array=false;
    }
    return($partidos_array);
}


?>