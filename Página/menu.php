<?php
session_start();

if (!isset($_SESSION["user"])) {
    header("Location: index.php");
    exit;
}
?>

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
            <img src="logobl.png">
            <ul>
                <li><a href="Transac.php">Historial de Transacciones</a></li>
                <li><a href="Usuario.php">Usuarios registrados</a></li>
                <li><a href="#">Transacciones Pendientes</a></li>
                <li><a href="#">Baneos y suspensiones</a></li>
                <li><a href="logout.php">Cerrar sesión</a></li> <!-- Moví este enlace dentro de la lista -->
            </ul>
        </nav>
    </header>
</body>
</html>
