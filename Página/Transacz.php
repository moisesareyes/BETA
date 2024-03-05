<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="stilou.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MA Pay | Admin</title>
</head>
    <body>

        <header>
            <nav>
                    <img src="logo1.png">
                <ul>
                    <li><a href="Menu.html">Inicio</a></li>
                    <li><a href="Users.php">Usuarios</a></li>
                    <li><a href="#">Prueba</a></li>
                    <li><a href="#">Prueba2</a></li>
                    <li><a href="#">Prueba3</a></li>
                </ul>
            </nav>
        </header>
<center>
<?php
include ("conex.php");


    $query="SELECT * FROM historial";
    $resul=mysqli_query($link, $query);

    echo "<table border>
    <tr>
    <td><b>ID</b>
    <td><b>Servidor</td>
    <td><b>Recep</td>
    <td><b>Tipo</td>
    <td><b>Moneda</td>
    <td><b>Status</td>
    <td><b>Cantidad</td>
    <td><b>Billetera1</td>
    <td><b>Billetera2</td>
    <td><b>Fecha</td>
    </tr>";

    while ($dato = mysqli_fetch_array($resul)){
        echo "<tr>";
        echo "<td>".$dato['ID']."</td>";
        echo "<td>".$dato['servidor']."</td>";
        echo "<td>".$dato['recep']."</td>";
        echo "<td>".$dato['tipo']."</td>";
        echo "<td>".$dato['moneda']."</td>";
        echo "<td>".$dato['status']."</td>";
        echo "<td>".$dato['cantidad']."</td>";
        echo "<td>".$dato['billetera1']."</td>";
        echo "<td>".$dato['billetera2']."</td>";
        echo "<td>".$dato['fecha']."</td>";
        echo "</tr>";
    }
    echo "</table>";
?>
