<?php
//データベースの接続
	require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Blog</title>
<style type="text/css">
	table,td,th{
		border:1px solid;
	}
</style>
</head>
<body>
<?php
try{
	//SQLの実行
    $sql = "SELECT * FROM blog where openflg=0 order by no desc";
	$sth = $dbh->prepare($sql);
	$sth->execute();

	//結果の表示
	while ($row = $sth->fetch(PDO::FETCH_ASSOC)) {
		echo "<table>";
		echo "<tr><td>".$row["no"]."</td></tr>";
		echo "<tr><td>".$row["title"]."</td></tr>";
		echo "<tr><td>".$row["body"]."</td></tr>";
        if (file_exists("./img/".$row["no"].".jpg")){
            echo "<tr><td><img src=./img/".$row["no"].".jpg width=500px>
            </td></tr>";
        }

		echo "<tr><td>".$row["date"]."</td></tr>";
		echo "</table>";
	}
}catch (Exception $e){
	echo ("Error:" . $e->getMessage());
}
?>

<p><a href="admin.php">管理ページ</a></p>
<a href="http://johodb.otemae.ac.jp/~zq16026s/">トップページに戻る</a>
</body>
</html>
<?php
//データベースの切断
$dbh = null;
?>
