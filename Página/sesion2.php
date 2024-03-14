<?php
include('conex.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST["user"];
    $pass = $_POST["pass"];
    $nom = $_POST["nom"];
    $cargo = $_POST["cargo"];

    // Verificar si el usuario ya existe
    $sql_select = "SELECT * FROM web WHERE user = ?";
    if ($stmt_select = $link->prepare($sql_select)) {
        $stmt_select->bind_param("s", $user);
        $stmt_select->execute();
        $result = $stmt_select->get_result();

        if ($result->num_rows > 0) {
            echo "El nombre de usuario ya está en uso.";
        } else {
            // Insertar nuevo usuario en la base de datos
            $sql_insert = "INSERT INTO web (user, pass, nom, cargo) VALUES (?, ?, ?, ?)";
            if ($stmt_insert = $link->prepare($sql_insert)) {
                // Hash de la contraseña utilizando SHA-256 antes de almacenarla en la base de datos
                $hashed_pass = password_hash($pass, PASSWORD_DEFAULT);
                $stmt_insert->bind_param("ssss", $user, $hashed_pass, $nom, $cargo);
                if ($stmt_insert->execute()) {
                    echo "Usuario registrado exitosamente.";
                } else {
                    echo "Error al registrar el usuario.";
                }
            } else {
                echo "Error en la preparación de la consulta.";
            }
        }
        $stmt_select->close();
    } else {
        echo "Error en la preparación de la consulta.";
    }
    $link->close();
}
?>

