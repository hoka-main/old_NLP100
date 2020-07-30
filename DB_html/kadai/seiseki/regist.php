<?php
//データベースの接続
require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>成績</title>
</head>
<body>
<?php
//エラー処理
if(!isset($_POST["shimei"])
    or !isset($_POST["kana"])
    or !isset($_POST["shiken"])
    or !isset($_POST["kokugo"])
    or !isset($_POST["shakai"])
    or !isset($_POST["rika"])
    or !isset($_POST["shakai"])
    ){
    exit("<p>未送信<br><a href=index.php>一覧へ戻る</a></p>");
}elseif(empty($_POST["shimei"])
    or empty($_POST["kana"])
    or empty($_POST["shiken"])
    or empty($_POST["kokugo"])
    or empty($_POST["sansuu"])
    or empty($_POST["rika"])
    or empty($_POST["shakai"])
    ){
    exit("<p>未入力<br><a href=index.php>一覧へ戻る</a></p>");
}



//受け取った値を変数に格納   
$shimei= htmlspecialchars($_POST["shimei"], ENT_QUOTES);
$kana= htmlspecialchars($_POST["kana"], ENT_QUOTES);
$shiken= htmlspecialchars($_POST["shiken"], ENT_QUOTES);
$kokugo = htmlspecialchars($_POST["kokugo"], ENT_QUOTES);
$sansuu = htmlspecialchars($_POST["sansuu"], ENT_QUOTES);
$rika = htmlspecialchars($_POST["rika"], ENT_QUOTES);
$shakai = htmlspecialchars($_POST["shakai"], ENT_QUOTES);

//SQLの実行
try {
	$sql = "INSERT INTO seiseki (shimei,kana,shiken,kokugo,sansuu,rika,shakai)
	VALUES (:shimeis,:kana,:shiken,:kokugo,:sansuu,:rika,:syakai)";
	$sth = $dbh->prepare($sql);
	$sth->bindParam(':no',$no,PDO::PARAM_INT);
	$sth->bindParam(":shimei", $shimei, PDO::PARAM_STR);
	$sth->bindParam(":kana", $kana, PDO::PARAM_STR);
	$sth->bindParam(":shiken", $shiken, PDO::PARAM_STR);
	$sth->bindParam(":kokugo", $kokugo, PDO::PARAM_INT);
	$sth->bindParam(":sansuu", $sansuu, PDO::PARAM_INT);
	$sth->bindParam(":rika", $rika, PDO::PARAM_INT);
	$sth->bindParam(":shakai", $shakai, PDO::PARAM_INT);
	$sth->execute();
	echo $sth->rowCount();// True or false確認
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
