<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>制作課題06-4</title>
</head>
<body>
<h1>
<?php
$dsn = 'mysql:dbname=zq16026s;host=localhost;charset=utf8mb4'; //接続する DB
$user ='zq16026s'; //ユーザー情報
$password = 'zq16026s'; //パスワード情報
変数 A = new PDO($dsn,$user,$password); //データベースに接続する命令
echo "<br>";
?>
<a href="http://johodb.otemae.ac.jp/~zq16026s/">トップページに戻る</a>
</h1>
</body>
</html>