<?php
//データベースの接続
	require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>成績</title>
<style type="text/css">
	table,td,th{
		border:1px solid;
	}
</style>
</head>
<body>
<h1>成績</h1>
<?php
try{
	//SQLの実行
	$sql = "SELECT * FROM seiseki";
	$sth = $dbh->prepare($sql);
	$sth->execute();

	//結果の表示
echo "<table><tr><td>連番</td><td>写真</td><td>氏名</td><td>カナ</td>
            <td>試験の種類</td><td>国語</td><td>算数</td><td>理科</td>
            <td>社会</td><td>編集</td><td>削除</td></tr>";
	while ($row = $sth->fetch(PDO::FETCH_ASSOC)) {
		echo "<tr>";
		echo "<td>".$row["no"]."</td>";
		echo "<td>".$row["photo"]."</td>";
		echo "<td>".$row["shimei"]."</td>";
		echo "<td>".$row["kana"]."</td>";
		echo "<td>".$row["shiken"]."</td>";
		echo "<td>".$row["kokugo"]."</td>";
		echo "<td>".$row["sansuu"]."</td>";
		echo "<td>".$row["rika"]."</td>";
		echo "<td>".$row["shakai"]."</td>";
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
