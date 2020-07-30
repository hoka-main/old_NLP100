<?php
	//データベース接続処理
	require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>成績</title>
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

//受け取ったnoを条件値にして、編集対象のレコード値を抽出するSQLを実行する
try {
$sql = "SELECT * FROM seiseki WHERE no=:no";
$sth=$dbh->prepare($sql);
$sth->bindParam(':no',$no,PDO::PARAM_INT);
$sth->execute();

	//結果の表示
	while ($row = $sth->fetch(PDO::FETCH_ASSOC)) {
        $shimei = $row["shimei"];
        $kana = $row["kana"];
        $shiken = $row["shiken"];
        $kokugo= $row["kokugo"];
        $sansuu = $row["sansuu"];
        $rika = $row["rika"];
        $shakai = $row["shakai"];
	}
}catch (Exception $e){
	echo ('Error:' . $e->getMessage());
}


?>
<h1>編集画面</h1>

<form action="update.php" method="post">
<fieldset>
    <p>連番：<?php echo "$no"; ?></p>
	<p>氏名：<input type="text" name="shimei"></p>
	<p>カナ：<input type="text" name="kana"></p>
	<p>種類：
		<select name='shiken'>
			<option value='shiken'>中間試験</option>
			<option value='shiken'>期末試験</option>
		</select>
	</p>
	<p>国語：<input type="text" name="kokugo"></p>
	<p>算数：<input type="text" name="sansuu"></p>
	<p>理科：<input type="text" name="rika"></p>
	<p>社会：<input type="text" name="shakai"></p>
	<p>写真：<input type="file" name="upfile" accept=".jpg" ></p>
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