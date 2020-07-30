<?php
	//データベース接続処理
	require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>愛読書</title>
</head>
<body>
<?php
//入力チェック、直接URLをアクセスされた場合の処理
if(!isset($_POST["title"]) or !isset($_POST["author"]) or !isset($_POST["price"])){
	exit("<p>未送信<br><a href=index.php>一覧へ戻る</a></p>");
}elseif(empty($_POST["title"]) or empty($_POST["author"]) or empty($_POST["price"])){
	exit("<p>未入力<br><a href=index.php>一覧へ戻る</a></p>");
}

//editform.phpから送られてきたデータを受け取り、各変数に格納する
$no = $_POST["no"];
$title = htmlspecialchars($_POST["title"]);
$author = htmlspecialchars($_POST["author"]);
$price = htmlspecialchars($_POST["price"]);

//受け取ったnoの値を条件にして、編集対象の値を抽出するSQLを実行する
try {
$sql="UPDATE booklist SET title=:title,author=:author,price=:price WHERE no=:no";
$sth=$dbh->prepare($sql);
$sth->bindParam(':no',$no,PDO::PARAM_INT);
$sth->bindParam(':title',$title,PDO::PARAM_STR);
$sth->bindParam(':author',$author,PDO::PARAM_STR);
$sth->bindParam(':price',$price,PDO::PARAM_INT);
$sth->execute();

}catch(Exception $e) {
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