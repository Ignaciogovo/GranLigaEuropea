<!-- <?php
// include_once('funciones.php');
// $calendario_array=select_calendario(1,2);
// foreach ($calendario_array as $jornada) {
//     echo "Jornada: " . $jornada['jornada'] . "<br>";
//     echo "Local: " . $jornada['local'] . " (ID: " . $jornada['id_local'] . ")<br>";
//     echo "Visitante: " . $jornada['visitante'] . " (ID: " . $jornada['id_visitante'] . ")<br>";
//     echo "<br>";
// }


//?> -->
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Partidos de la Liga</title>
</head>
<body>
  <?php
    include_once("funciones.php");

    $jornada = 5; // Cambia esto al número de jornada deseado
    $temporada = 2; // Cambia esto a la temporada deseada

    $partidos = select_partidos($jornada, $temporada);

    if ($partidos !== false) {
foreach ($partidos as $partido) {
  echo "<tr>
          <td><span class='bold'>{$partido['local']} <strong>{$partido['goles_local']}-{$partido['goles_visitante']}</strong> {$partido['visitante']}</span></td>
          <td>{$partido['arbitro']}</td>
          <td> {$partido['aforo']}</td>
        </tr>";

}

echo "</table>";
      } else {
        echo "No se encontraron partidos para la jornada $jornada de la temporada $temporada.";
      }
  ?>
</body>
</html>