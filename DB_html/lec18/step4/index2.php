<?php
//データベースの接続
	require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Blog</title>
<style type="text/css">
*{
  margin: 0;
  padding: 0;
}

body{
	background-color:#f0f8ff;	
}

#container{
	width:1000px;
	margin-left:auto;
	margin-right:auto;
}

table{
	margin:10 0 10 0;
	background-color:#ffffff;
	width: 100%;
	margin-right: auto;
	margin-left: auto;
	padding 3px;
	border: 3px solid #dcdcdc;
	border-spacing: 0;
	border-collapse: separate;
	border-radius: 10px;
	-webkit-border-radius: 10px;
	-moz-border-radius: 10px;
}

.title{
	font-size:24px;
	font-weight: bold;
	background-color:#dcdcdc;
	background-image:url("./img/header/mark.png");
	background-repeat: no-repeat;
	padding:5 70 5 70;
}

.body{
	font-size:20px;
	color:#696969;
	letter-spacing: 2px;
	padding:10 70 10 70;
}

.photo{
	text-align:center;
}

.date{
	font-size:16px;
	text-align:right;
	color:#696969;
	padding:10 10 10 0;
}

</style>
</head>
<body>
<div id="container">
<p><img src="./img/header/header.jpg"></p>
<?php
try{
	//SQLの実行
	$sql = "SELECT * FROM blog where openflg=0 order by no desc";
	$sth = $dbh->prepare($sql);
	$sth->execute();

	//結果の表示
	while ($row = $sth->fetch(PDO::FETCH_ASSOC)) {
		echo "<table>";
		echo "<tr><td class=title>".$row["title"]."</td></tr>";
		echo "<tr><td class=body>".$row["body"]."</td></tr>";
		if (file_exists("./img/".$row["no"].".jpg")){
			echo "<tr><td class=photo><img src=./img/".$row["no"].".jpg width=500px></td></tr>";
		}
		echo "<tr><td class=date>記事".$row["no"]."　".$row["date"]."</td></tr>";
		echo "</table>";
	}
}catch (Exception $e){
	echo ("Error:" . $e->getMessage());
}
?>

<p><a href="admin.php">管理ページ</a></p>
</div>
</body>
</html>
<?php
//データベースの切断
$dbh = null;
?>
