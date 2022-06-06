<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Número de </title>
</head>
<body>

</body>
</html>
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>GranLigaEuropea</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Spartan:wght@400;600&display=swap" rel="stylesheet">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<?php
?>
<body>
    <section class="mb-5">
        <header class="bg-dark text-light p-2 ">
            <nav class="navbar navbar-expand-lg">
                <div class="container-fluid">
                    <!-- <a class="navbar-brand" href="#">Navbar w/ text</a> -->
                    <span class="navbar-text ms-5">
                        <h1>Gran liga europea</h1>
                    </span>
                    <div class="collapse navbar-collapse" id="navbarText">
                        <ul class="navbar-nav ms-auto me-4 mb-2 mb-lg-0">
                            <li class="nav-item">
                                <a class="active link-warning" aria-current="page" href="index.php">Inicio</a>
                            </li>
                            <li class="nav-item">
                                <a class="m-3 link-warning" href="estadisticas.php">Estadisticas</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="row">
                <div class="col-6">
                </div>
            </div>
        </header>
        <div>
        </body>

</html><?php
echo "<a href='index.php'>Página inicial</a><br>";
$jornada=$_POST["jornada"];
$participantes = 20;
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
        planificacionjornadas($participantes,$primeros,$array1,$array2,$jornada);
    }
    
?>
        </div>

    </section>
    <!-- footer -->
    <footer class="text-center bg-light mt-auto">
        <div class="row pt-5 g-0">
            <div class="col-12">
                <div class="row g-0">
                    <div class="col-4">
                    </div>
                    <div class="col-4">
                        <div class="row">
                            <div class="col-12 pb-4 text-dark">
                                <h6>Enlaces</h6>
                            </div>
                            <div class="col-12 col-sm-4 m-auto">
                                <a href="https://github.com/Ignaciogovo" class="link-warning">github</a>
                            </div>
                            <div class="col-12 col-sm-4 m-auto">
                                <a href="https://twitter.com/granligaeuropa" class="link-warning">twitter</a>
                            </div>
                            <div class="col-12 col-sm-4 m-auto">
                                <a href="https://po.ta.to/" class="link-warning">linkedln</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-4">
                    </div>
                </div>
            </div>
            <div class="col-12 mt-5 bg-secondary">
                <div class="text-light">© 2022 Copyright:
                    <a class="link-warning" href="https://github.com/Ignaciogovo">Ignaciogovo</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
