<?php
//データベースの接続
require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>愛読書</title>
</head>
<body>
<?php
//エラー処理
if(!isset($_POST["title"])
    or !isset($_POST["author"])
    or !isset($_POST["price"])
    ){
	exit("<p>未送信<br><a href=index.php>一覧へ戻る</a></p>");
}elseif(
    empty($_POST["title"])
    or empty($_POST["author"])
    or empty($_POST["price"])
    ){
	exit("<p>未入力<br><a href=index.php>一覧へ戻る</a></p>");
}



//受け取った値を変数に格納   
$title= htmlspecialchars($_POST["title"], ENT_QUOTES);
$author = htmlspecialchars($_POST["author"], ENT_QUOTES);
$price = htmlspecialchars($_POST["price"], ENT_QUOTES);

//SQLの実行
try {
	$sql = "INSERT INTO booklist (title,author,price) VALUES (:title,:author,:price)";
	$sth = $dbh->prepare($sql);
	$sth->bindParam(":title", $title, PDO::PARAM_STR);
	$sth->bindParam(":author", $author, PDO::PARAM_STR);
	$sth->bindParam(":price", $price, PDO::PARAM_INT);
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
