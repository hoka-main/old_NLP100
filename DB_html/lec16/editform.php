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
//直接URLをアクセスされた場合の処理
if(!isset($_POST["no"])){
	exit("<p>未送信<br><a href=index.php>一覧へ戻る</a></p>");
}elseif(empty($_POST["no"])){
	exit("<p>未入力<br><a href=index.php>一覧へ戻る</a></p>");
}

//index.phpから送られてきたデータ（no）を受け取り、$noに格納する


//受け取ったnoを条件値にして、編集対象のレコード値を抽出するSQLを実行する
try {
$sql = "SELECT * FROM classmate WHERE no=:no";
$sth=$dbh->prepare($sql);
$sth->bindParam(':no',$no,PDO::PARAM_INT);
$sth->execute();

	//結果の表示
	while ($row = $sth->fetch(PDO::FETCH_ASSOC)) {
        $name = $row["name"];
        $age = $row["age"];
	}
}catch (Exception $e){
	echo ('Error:' . $e->getMessage());
}


?>
<h1>編集画面</h1>

<form action="update.php" method="post">
<fieldset>
<p>連番：<?php echo "$no"; ?></p>
<p>名前：<input type="text" name="name" value="<? php echo "$name"; ?>"></p>
<p>年齢：<input type="text" name="age" value="<?php echo "$age"; ?>"></p>
 <input type="hidden" name="no" value="<?php echo "$no"; ?>">
 <input type="submit" value="更新する">
 </fieldset>
</form>

<p><a href="index.php">一覧へ戻る</a></p>
</body>
</html>
<?php
//データベースの切断
$dbh = null;
?>