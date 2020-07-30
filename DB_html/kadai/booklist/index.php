<?php
//データベースの接続
	require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>愛読書</title>
<style type="text/css">
	table,td,th{
		border:1px solid;
	}
</style>
</head>
<body>
<h1>愛読書</h1>
<?php
try{
	//SQLの実行
	$sql = "SELECT * FROM booklist";
	$sth = $dbh->prepare($sql);
	$sth->execute();

	//結果の表示
echo "<table><tr><td>連番</td><td>タイトル</td><td>著者</td><td>価格</td><td></td>
<td></td></tr>";
	while ($row = $sth->fetch(PDO::FETCH_ASSOC)) {
		echo "<tr>";
		echo "<td>".$row["no"]."</td>";
		echo "<td>".$row["title"]."</td>";
		echo "<td>".$row["author"]."</td>";
		echo "<td>".$row["price"]."</td>";
		echo "<td><form action=editform.php method=POST>
            <input type=hidden name=no value=" . $row["no"] . ">
            <input type=submit value=編集></form></td>";
        echo "<td><form action=delete.php method=POST>
            <input type=hidden name=no value=" . $row["no"] . ">
            <input type=submit value=削除></form></td>";
		echo "</tr>";
	}
	echo "</table>";
}catch (Exception $e){
	echo ("Error:" . $e->getMessage());
}
?>

<p><a href="form.html">レコードの追加</a></p>
<a href="http://johodb.otemae.ac.jp/~zq16026s/">トップページに戻る</a>
</body>
</html>
<?php
//データベースの切断
$dbh = null;
?>
