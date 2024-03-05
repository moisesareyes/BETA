<?php
include ("conex.php");
if($link){
    $user=$_POST["user"];

    $clave=$_POST["pass"];








    $query="SELECT * FROM test where user='".$user."' and '".$clave."'";

    
    $resul=mysqli_query($link, $query);

    print_r($resul);



    if (!empty($_POST["btn"])) {
        if (empty($_POST["user"]) and empty($_POST["pass"])) {
            echo "Los campos están vacios";
        } else {
            $user=$POST["user"];
            $pass=$POST["pass"];
        if ($datos=$resul->fetch_object()) {
header("Menu.php");
        } else {
        }
        }
    }
}