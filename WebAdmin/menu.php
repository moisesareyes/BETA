<?php
session_start();

if (!isset($_SESSION["user"])) {
    header("Location: index.php");
    exit;
}

include "conex.php";

if ($link->connect_error) {
    die("La conexión a la base de datos ha fallado: " . $link->connect_error);
}

$cons = "SELECT nom FROM web WHERE user = '" . $_SESSION["user"] . "'";
$resuln = $link->query($cons);

if (!$resuln) {
    die("Error en la consulta: " . $link->error);
}

if ($resuln->num_rows > 0) {
    $fila = $resuln->fetch_assoc();
    $nomb = $fila["nom"];
} else {
    $nomb = "Nombre Desconocido";
}

$link->close();
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="stilou.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MA Pay | Admin</title>
    <style>
        body {
            position: relative;
        }
        .welcome-text {
            position: absolute;
            bottom: 1px;
            left: 85px;
            font-size: 14px;
            font-family: "Sora", sans-serif;
            color: #fff;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <img src="logobl.png">
            <ul>
                <li><a href="Transac.php">Historial de Transacciones</a></li>
                <li><a href="Usuario.php">Usuarios registrados</a></li>
                <li><a href="pendi.php">Transacciones Pendientes</a></li>
                <li><a href="bans.php">Baneos y suspensiones</a></li>
                <li><a href="logout.php">Cerrar sesión</a></li>
            </ul>
        </nav>
    </header>
    <p class="welcome-text">Bienvenido, <?php echo $nomb; ?></p>
</body>
</html>

