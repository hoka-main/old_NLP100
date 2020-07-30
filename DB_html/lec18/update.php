<?php
	//データベース接続処理
	require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Blog</title>
</head>
<body>
<?php
//入力チェック、直接URLをアクセスされた場合の処理
if(!isset($_POST["openflg"])){
    exit("<p>未送信<br><a href=admin.php>一覧へ戻る</a></p>");
}
//admin.phpから送られてきたデータを受け取り、各変数に格納する
$no = $_POST["no"];
$openflg = $_POST["openflg"];



//受け取ったnoの値を条件にして、編集対象のレコードを更新するSQLを実行する
try {
    $sql="UPDATE blog SET openflg=:openflg WHERE no=:no";
    $sth=$dbh->prepare($sql);
    $sth->bindParam(':no',$no,PDO::PARAM_INT);
    $sth->bindParam(':openflg',$openflg,PDO::PARAM_INT);
    $sth->execute();

	//データベースの切断
    $dbh = null;



	//リダイレクト

    header("Location: ./admin.php");

	
}catch(Exception $e) {
	echo ("Error:" . $e->getMessage());
}

?>
</body>
</html>
