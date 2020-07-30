<?php
//データベースの接続
	require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>社員名簿</title>
<style type="text/css">
	table,td,th{
		border:1px solid;
	}
</style>
</head>
<body>
<h1>社員名簿</h1>
<?php
try{
	//SQLの実行
	$sql = "SELECT * FROM employee";
	$sth = $dbh->prepare($sql);
	$sth->execute();

	//結果の表示
	echo "<table><tr><td>連番</td><td>氏名</td><td>年齢</td></tr>";
	while ($row = $sth->fetch(PDO::FETCH_ASSOC)) {
		echo "<tr>";
echo "<td>" . $row["no"] . "</td>";
echo "<td>" . $row["emp_id"] . "</td>";
echo "<td>" . $row["name"] . "</td>";
echo "<td>" . $row["gender"] . "</td>";
echo "<td>" . $row["birthday"] . "</td>";
echo "<td>" . $row["salary"] . "</td>";
echo "</tr>";
	}
	echo "</table>";
}catch (Exception $e){
	echo ("Error:" . $e->getMessage());
}
?>

<hr>
<p><a href="form.html">レコードの追加</a></p>
<a href="http://johodb.otemae.ac.jp/~zq16026s/">トップページに戻る</a>
</body>
</html>
<?php
//データベースの切断
$dbh = null;
?>
