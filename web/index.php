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
                                <a class="active link-warning" aria-current="page" href="#">Disabled</a>
                            </li>
                            <li class="nav-item">
                                <a class="m-3 link-warning" href="#clasificacion">Clasificación</a>
                            </li>
                            <li class="nav-item">
                                <a class="link-warning" href="estadisticas.php">Estadisticas</a>
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
        <div class="container mt-5 mb-5">
        <h1 class ="m-3" id="clasificacion">Clasificación</h1>
        <div class="row">
            <div class="col">
                <table class="table table-striped mb-t">
                    <thead>
                        <tr class="p-4">
                            <th scope="col">Puesto</th>
                            <th scope="col">Club</th>
                            <th scope="col">puntos</th>
                            <th scope="col">A favor</th>
                            <th scope="col">En contra</th>
                            <th scope="col">+-Goles</th>
                            <th scope="col">Ganados</th>
                            <th scope="col">Empatados</th>
                            <th scope="col">Perdidos</th>
                        </tr>
                    </thead>
                    <tbody>
<?php 
                    include_once("funciones.php");
                    clasificacion();
?>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <div class="container mt-5 mb-5">
        <h1 class ="m-3">Máximos goleadores de la temporada</h1>
        <div class="row">
            <div class="col">
                <table class="table table-striped mb-t table-expand-lg">
                    <thead>
                        <tr class="p-4">
                            <th scope="col"></th>
                            <th scope="col">Nombre</th>
                            <th scope="col">Goles</th>
                            <th scope="col">asistencias</th>
                            <th scope="col">Amarillas</th>
                            <th scope="col">Rojas</th>
                            <th scope="col ">Titular</th>
                            <th scope="col">Partidos</th>
                            <th scope="col">Posicion</th>
                            <th scope="col">Valor</th>
                            <th scope="col">Club</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php 
                            include_once("funciones.php");
                        EstadisticasTotales();
                        ?>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
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
                                <a href="https://www.linkedin.com/in/ignacio-govantes-ojeda-0b1869220/" class="link-warning">linkedln</a>
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
</body>

</html>