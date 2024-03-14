<?php
$user=$_POST['user'];
$pass=$_POST['pass'];
session_start();
$SESSION['user']=$user;

include('conex.php');

$cons="SELECT*FROM test where user='$user' and pass='$pass'";
$res=mysqli_query($link, $cons);
$filas=mysqli_num_rows($res);

if($filas){
    header("location:menu.php");

}else{
    ?>
    <?php
    include("index.php");
    ?>
</div>
    <?php
}
mysqli_free_result($res);
mysqli_close($link);