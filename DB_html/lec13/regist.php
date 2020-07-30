<?php
//データベースの接続
$con = 'mysql:dbname=zq16026s;host=localhost;charset=utf8mb4';
$user = 'zq16026s';
$password = 'zq16026s';
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>クラスメイト</title>
</head>
<body>
<?php
//form.htmlから送られてきた値を受け取る


//データベースに値を登録する処理
try {
$sql = "INSERT INTO classmate (name,age) VALUES (:name,:age)"; //①
$sth = $dbh->prepare($sql); //②
$sth->bindParam(":name", $name, PDO::PARAM_STR); //③
$sth->bindParam(":age", $age, PDO::PARAM_INT); //④
$sth->execute(); //⑤

} catch(Exception $e) {
	echo ("Error:" . $e->getMessage());
}

?>
<p><a href="index.php">一覧へ戻る</a></p>
</body>
</html>
<?php
//データベースの切断
$dbh = null;
?>

