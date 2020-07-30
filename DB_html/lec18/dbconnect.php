<?php
$con = 'mysql:dbname=zq16026s;host=localhost;charset=utf8mb4';
$user = 'zq16026s';
$password = 'zq16026s';
try {
	$dbh = new PDO($con , $user , $password);
} catch (PDOException $e){
	die ('Connect Error:' . $e->getCode());
}
?>
