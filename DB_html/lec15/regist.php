<?php
//データベースの接続
require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>社員名簿</title>
</head>
<body>
<?php
//エラー処理
if(!isset(
$_POST["emp_id"])
or !isset($_POST["name"])
or !isset($_POST["gender"])
or !isset($_POST["birthday"])
or !isset($_POST["salary"])
){
 exit("<p>未送信<br><a href=index.php>一覧へ戻る</a></p>");
}elseif(
empty($_POST["emp_id"])
or empty($_POST["name"])
or empty($_POST["gender"])
or empty($_POST["birthday"])

or empty($_POST["salary"])
){
 exit("<p>未入力<br><a href=index.php>一覧へ戻る</a></p>");
}



//受け取った値を変数に格納   
$emp_id = htmlspecialchars($_POST["emp_id"], ENT_QUOTES);
$name = htmlspecialchars($_POST["name"], ENT_QUOTES);
$gender = htmlspecialchars($_POST["gender"], ENT_QUOTES);
$birthday = htmlspecialchars($_POST["birthday"], ENT_QUOTES);
$salary = htmlspecialchars($_POST["salary"], ENT_QUOTES);

//SQLの実行
try {
$sql = "INSERT INTO employee (emp_id,name,gender,birthday,salary) VALUES
(:emp_id,:name,:gender,:birthday,:salary)";
$sth = $dbh->prepare($sql);
$sth->bindParam(":emp_id ", $emp_id, PDO::PARAM_STR);
$sth->bindParam(":name", $name, PDO::PARAM_STR);
$sth->bindParam(":gender", $gender, PDO::PARAM_STR);
$sth->bindParam(":birthday ", $birthday, PDO::PARAM_STR);
$sth->bindParam(":salary ", $salary, PDO::PARAM_INT);
	$sth->execute();
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
