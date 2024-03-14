<?php
include('conex.php');
if ($link->connect_error) {
    die("Conexión fallida: " . $link->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener los datos del formulario
    $user = $_POST["user"];
    $pass = $_POST["pass"];

    // Verificar si algún campo está vacío
    if (empty($user) || empty($pass)) {
        $mensaje_error = "Por favor, completa todos los campos.";
    } else {
        // Consultar la base de datos para verificar las credenciales
        $sql = "SELECT * FROM test WHERE user = '$user' AND pass = '$pass'";
        $result = $link->query($sql);

        if ($result->num_rows > 0) {
            // Las credenciales son correctas, redirigir a la página de inicio
            header("Location: menu.php");
            exit();
        } else {
            // Las credenciales son incorrectas, mostrar un mensaje de error
            $mensaje_error = "Nombre de usuario o contraseña incorrectos.";
        }
    }
}

$link->close();
include("index.php");
?>

    <h2>Error de inicio de sesión</h2>
    <p><?php echo $mensaje_error; ?></p>
    <p><a href="index.php">Volver al formulario de inicio de sesión</a></p>
