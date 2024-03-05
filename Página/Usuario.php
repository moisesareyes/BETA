<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="stilou.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MA Pay | Registros</title>
</head>
    <body>

        <header>
            <nav>
                    <img src="logobl.png">
                <ul>
                    <li><a href="Menu.html">Inicio</a></li>
                    <li><a href="Transac.php">Historial de Transacciones</a></li>
                    <li><a href="#">Transacciones Pendientes</a></li>
                    <li><a href="#">Baneos y suspensiones</a></li>
                    <li><a href="#">Salir</a></li>
                </ul>
            </nav>
        </header>

        <table class="table table-light">
              <tr>
                <th scope="col">ID</th>
                <th scope="col">User ID</th>
                <th scope="col">Nombre</th>
                <th scope="col">Apellido</th>
                <th scope="col">User Name</th>
                <th scope="col">Email</th>
                <th scope="col">Teléfono</th>
                <th scope="col">Fecha de Registro</th>
              </tr>
            </thead>
            <tbody>
              <?php require_once 'conexu.php' ?>
              <tr></tr>
            </tbody>
          </table>