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
                    <li><a href="Transac.php">Transacciones</a></li>
                    <li><a href="#">Prueba</a></li>
                    <li><a href="#">Prueba2</a></li>
                    <li><a href="#">Prueba3</a></li>
                </ul>
            </nav>
        </header>
<center>
<?php
include ("conex.php");


    $query="SELECT * FROM usuario";
    $resul=mysqli_query($link, $query);

    echo "<table border>
    <tr>
    <td><b>ID</b>
    <td><b>UserID</td>
    <td><b>Nombre</td>
    <td><b>Apellido</td>
    <td><b>User Name</td>
    <td><b>Email</td>
    <td><b>Pass</td>
    <td><b>Tlf</td>
    <td><b>Fecha de Registro</td>
    </tr>";

    while ($dato = mysqli_fetch_array($resul)){
        echo "<tr>";
        echo "<td>".$dato['ID']."</td>";
        echo "<td>".$dato['UserID']."</td>";
        echo "<td>".$dato['Nombre']."</td>";
        echo "<td>".$dato['Apellido']."</td>";
        echo "<td>".$dato['User_name']."</td>";
        echo "<td>".$dato['Email']."</td>";
        echo "<td>".$dato['Pass']."</td>";
        echo "<td>".$dato['Tlf']."</td>";
        echo "<td>".$dato['Reg']."</td>";
        echo "</tr>";
    }
    echo "</table>";
?>
