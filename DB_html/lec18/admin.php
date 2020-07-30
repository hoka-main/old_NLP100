<?php
//データベースの接続
require_once "./dbconnect.php";
?>
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Blog</title>
<style type="text/css">
	body{
		width:800px;
	}
	
	table,td,th{
		border:1px solid;
	}
	
	table{
		margin:10 0 10 0;
		width:100%;
	}
	
	td:nth-child(1) {
		width:100px;
	}

</style>
</head>
<body>

<h1>管理画面</h1>
<form action="regist.php" method="POST" enctype="multipart/form-data">
<fieldset>
<p>表題：<input type="text" name="title" size="100"></p>
<p>本文：<textarea name="body" rows="10" cols="100"></textarea></p>
<p>写真：<input type="file" name="upfile" accept=".jpg" ></p>
<input type="submit" value="投稿する">
</fieldset>
</form>

<?php
try{
	//SQLの実行
    $sql = "SELECT * FROM blog order by no desc"; //新しい記事を上に表示する
    $sth = $dbh->prepare($sql);
    $sth->execute();

	//結果の表示
    while ($row = $sth->fetch(PDO::FETCH_ASSOC)) {
        //1 つのレコードに対して 1 つのテーブルを作成する
        echo "<table>";
        echo "<tr><td>公開</td>";
        echo "<td><form action=update.php method=POST>";
        echo "<select name=openflg><option value=0";
        if($row["openflg"]==0){echo " selected ";}
        echo ">公開</option><option value=1";
        if($row["openflg"]==1){echo " selected ";}
        echo ">非公開</option></select>";
        echo "<input type=hidden name=no value=";
        echo $row["no"];
        echo "><input type=submit value=更新 ></form>";
        echo "</td></tr>";
        echo "<tr><td>No</td><td>" .$row["no"]. "</td></tr>";
        echo "<tr><td>表題</td><td>" .$row["title"]. "</td></tr>";
        if (file_exists("./img/".$row["no"].".jpg")){
        echo "<tr><td>画像</td>
            <td><img src=./img/".$row["no"].".jpg width=300px></td></tr>";
        }
        echo "<tr><td>本文</td><td>" .$row["body"]. "</td></tr>";
        echo "<tr><td>日付</td><td>" .$row["date"]. "</td></tr>";
        echo "</table>";
    }
}catch (Exception $e){
	echo ("Error:" . $e->getMessage());
}
?>
</body>
</html>
<?php
//データベースの切断
$dbh = null;
?>
