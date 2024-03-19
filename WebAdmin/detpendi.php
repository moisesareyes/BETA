<?php
// Incluir archivo de conexión
include "conex.php";

if ($link->connect_error) {
    die("Conexión fallida: " . $link->connect_error);
}

// Obtener el ID de la operación seleccionada
$elemento_id = $_GET["id"];

// Consulta SQL para obtener los detalles de la operación seleccionada
$sql = "SELECT * FROM recarga WHERE id = $elemento_id";
$result = $link->query($sql);

if ($result->num_rows > 0) {
    // Output de detalles de la operación
    $row = $result->fetch_assoc();
    echo "<h3>Detalles de la operación:</h3>";
    echo "<p>Operación: " . $row["operacion"] . "</p>";
    echo "<p>Usuario: " . $row["usuario"] . "</p>";
    echo "<p>Documento: " . $row["doc"] . "</p>";
    echo "<p>Formato: " . $row["formato"] . "</p>";
    echo "<p>Teléfono: " . $row["telefono"] . "</p>";
    echo "<p>Moneda: " . $row["tipo"] . "</p>";
    echo "<p>Cantidad: " . $row["cantidad"] . "</p>";
} else {
    echo "<p>No se encontraron detalles para la operación seleccionada.</p>";
}

$link->close();
?>
