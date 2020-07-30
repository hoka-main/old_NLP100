<?php
	//データベース接続処理
	require_once './dbconnect.php';
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>愛読書</title>
</head>
<body>
<?php
//直接URLをアクセスされた場合の処理
if(!isset($_POST["no"])){
exit("<p>未送信<br><a href=index.php>一覧へ戻る</a></p>");
}elseif(empty($_POST["no"])){
exit("<p>未入力<br><a href=index.php>一覧へ戻る</a></p>");
}

//index.phpから送られてきたデータ（no）を受け取り、$noに格納する
$no = $_POST["no"];

//受け取ったnoを条件値にして対象のレコードを削除するSQLを実行する
try {
$sql="DELETE FROM booklist WHERE no=:no";
$sth=$dbh->prepare($sql);
$sth->bindParam(':no',$no,PDO::PARAM_INT);
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