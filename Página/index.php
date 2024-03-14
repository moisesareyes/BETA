<?php
include('conex.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST["user"];
    $pass = $_POST["pass"];

    if (empty($user) || empty($pass)) {
        $mensaje_error = "Por favor, completa todos los campos.";
    } else {
        // Busca el usuario en la base de datos
        $sql = "SELECT * FROM web WHERE user = ?";
        if ($stmt = $link->prepare($sql)) {
            $stmt->bind_param("s", $user);
            $stmt->execute();
            $result = $stmt->get_result();

            if ($result->num_rows == 1) {
                $row = $result->fetch_assoc();
                // Verifica la contraseña
                if (password_verify($pass, $row['pass'])) {
                    // Inicia sesión
                    session_start();
                    $_SESSION["user"] = $user;
                    // Redirige al usuario al panel de control
                    header("Location: menu.php");
                    exit();
                } else {
                    $mensaje_error = "Usuario o contraseña incorrectos.";
                }
            } else {
                $mensaje_error = "Usuario o contraseña incorrectos.";
            }
            $stmt->close();
        } else {
            $mensaje_error = "Error en la consulta.";
        }
    }
    $link->close();
}
?>

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
        <form method="POST">
            <h1>MA Pay | Admin</h1>
            <div class="input-box">
                <input id="user" type="text" class="input" name="user" placeholder="Usuario" required>
                <i class="bx bxs-user"></i>
            </div>
            <div class="input-box">
                <input type="password" id="input" class="input" name="pass" placeholder="Contraseña" required>
                <i class="bx bxs-lock-alt"></i>
            </div>
            <div class="bt"></div>
            <input type="submit" class="btn" value="Iniciar Sesión" name="btn">
            <div class="reg"></div>
            <?php
            if (isset($mensaje_error)) {
                echo "<p>$mensaje_error</p>";
            }
            ?>
        </form>
    </div>
</body>
</html>
