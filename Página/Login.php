<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="sti.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MA Pay | Admin</title>
</head>
    <body>

        <div class="logo">
            <img src="blancma.png">

        </div>

    <div class="fondo">
    <form method="post" action="">
        <h1>MA Pay | Admin</h1>
        <?php
        include("conexl.php");
        ?>
        <div class="input-box">
            <input id="user" type="text" class="input" name="user" placeholder="Usuario" requiered>
            <i class="bx bxs-user"></i>
            </div>

            <div class="input-box">
                <input type="password" id="input" class="input" name="pass" placeholder="Contraseña" requiered>
                <i class="bx bxs-lock-alt"></i>
            </div>

            <div class="olvidar-recordar">
            </div>

            <button type="submit" class="btn">Iniciar Sesión</button>
            <div class="registrar-link"></div>
    </form>
</div>
</body>
</html>