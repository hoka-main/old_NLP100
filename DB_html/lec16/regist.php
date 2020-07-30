<?php
//データベースの接続
require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>クラスメイト</title>
</head>
<body>
<?php
//エラー処理
if(!isset($_POST["name"]) or !isset($_POST["age"])){
    exit("<p>未送信<br><a href=index.php>一覧へ戻る</a></p>");
}elseif(empty($_POST["name"]) or empty($_POST["age"])){
    exit("<p>未入力<br><a href=index.php>一覧へ戻る</a></p>");
}



//受け取った値を変数に格納   
$name= htmlspecialchars($_POST["name"], ENT_QUOTES);
$age = htmlspecialchars($_POST["age"], ENT_QUOTES);

//SQLの実行
try {
	$sql = "INSERT INTO classmate (name,age) VALUES (:name,:age)";
	$sth = $dbh->prepare($sql);
	$sth->bindParam(":name", $name, PDO::PARAM_STR);
	$sth->bindParam(":age", $age, PDO::PARAM_INT);
	$sth->execute();
} catch(Exception $e) {
	echo ("Error:" . $e->getMessage());
}
?>
<p><a href="index.php">一覧へ戻る</a></p>
</body>
</html>
<?php
$dbh = null;
?>
