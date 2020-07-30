<?php
	//データベース接続処理
	require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>クラスメイト</title>
</head>
<body>
<?php
//入力チェック、直接URLをアクセスされた場合の処理
if(!isset($_POST["name"]) or !isset($_POST["age"])){
	exit("<p>未送信<br><a href=index.php>一覧へ戻る</a></p>");
}elseif(empty($_POST["name"]) or empty($_POST["age"])){
	exit("<p>未入力<br><a href=index.php>一覧へ戻る</a></p>");
}

//editform.phpから送られてきたデータを受け取り、各変数に格納する


//受け取ったnoの値を条件にして、編集対象の値を抽出するSQLを実行する
try {
$sql="UPDATE classmate SET name=:name,age=:age WHERE no=:no";
$sth=$dbh->prepare($sql);
$sth->bindParam(':no',$no,PDO::PARAM_INT);
$sth->bindParam(':name',$name,PDO::PARAM_STR);
$sth->bindParam(':age',$age,PDO::PARAM_INT);
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