<?php
//データベースの接続
$con = 'mysql:dbname=zq16026s;host=localhost;charset=utf8mb4';
$user = 'zq16026s';
$password = 'zq16026s';
try {
 $dbh = new PDO($con , $user , $password);
} catch (PDOException $e){
 die ('Connect Error:' . $e->getCode());
}
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>クラスメイト</title>
</head>
<body>
<h1>クラスメイト</h1>
<?php
try{
	//SQLの実行
$sql = "SELECT * FROM classmate";
$sth = $dbh->prepare($sql);
$sth->execute();

	//結果の表示
echo "<table>";
while ($row = $sth->fetch(PDO::FETCH_ASSOC)) {
echo "<tr>";
echo "<td>" . $row["no"] . "</td>";
echo "<td>" . $row["name"] . "</td>";
echo "<td>" . $row["age"] . "</td>";
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
