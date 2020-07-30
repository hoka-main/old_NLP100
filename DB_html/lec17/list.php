<?php
	require_once "dbconnect.php";
?>
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>ユーザーリスト</title>
<script type="text/javascript">
<!--
// -->
</script>
<style type="text/css">
table,th,td{
	border:solid black 1px;
}

table{
	width:500px;
}
.sortbtn{
    float:right;
}
</style>
</head>
<body>
<a href="http://johodb.otemae.ac.jp/~zq16026s/">トップページに戻る</a>
<form action="list.php" method="POST">
<fieldset>
    <p>氏名：<input type="text" name="keyword" size="20" value="" ></p>
    <input type="submit" value="検索する" >
</fieldset>
</form>

<?php
//入力チェックと初期値の設定

if(!isset($_POST["keyword"]) or empty($_POST["keyword"])){
    $keyword = "%";
}else{
    $keyword = htmlspecialchars($_POST["keyword"], ENT_QUOTES);
    $keyword = "%" . $keyword . "%";
}
//sort の初期値
if (!isset($_POST["sort"])){
    $sort = "asc";
    $sortkey = "no";
}else{
    $sort = $_POST["sort"];
    $sortkey = $_POST["sortkey"];
}

try {
    //SQLの実行
    $sql = "SELECT * FROM userlist WHERE name like :keyword ORDER BY $sortkey $sort";
    $sth = $dbh->prepare($sql);
    $sth->bindParam(":keyword", $keyword, PDO::PARAM_STR);
    $sth -> execute();

    //結果の表示
    $count = $sth->rowCount();
    if($count>0){ //検索結果があれば結果を表示
        //表ヘッダーにボタンを設置
        echo "<table><tr>
            <th>No
                <form class=sortbtn action=list.php method=POST>
                    <input type=hidden name=sortkey value=no>
                    <input type=hidden name=sort value=asc>
                    <input type=hidden name=keyword value=$keyword>
                    <input type=submit value=昇>
                </form>
                <form class=sortbtn action=list.php method=POST>
                    <input type=hidden name=sortkey value=no>
                    <input type=hidden name=sort value=desc>
                    <input type=hidden name=keyword value=$keyword>
                    <input type=submit value=降>
                </form>
            </th>
            <th>Name</th>
            <th>Age
                <form class=sortbtn action=list.php method=POST>
                    <input type=hidden name=sortkey value=age>
                    <input type=hidden name=sort value=asc>
                    <input type=hidden name=keyword value=$keyword>
                    <input type=submit value=昇>
                </form>
                <form class=sortbtn action=list.php method=POST>
                    <input type=hidden name=sortkey value=age>
                    <input type=hidden name=sort value=desc>
                    <input type=hidden name=keyword value=$keyword>
                    <input type=submit value=降>
                </form>
            </th>
            </tr>";
    while($row = $sth->fetch(PDO::FETCH_ASSOC)){
        echo "<tr>";
        echo "<td>".$row["no"]."</td>";
        echo "<td>".$row["name"]."</td>";
        echo "<td>".$row["age"]."</td>";
        echo "</tr>";
    }
       echo "</table>";
    }else{ //検索結果がなければメッセージを表示
        exit("<p>該当レコードなし<br><a href=form.html>検索画面へ戻る</a></p>");
    }
}catch (Exception $e){
        echo ('Error:' . $e->getMessage());
}?>
    
</body>
</html>
<?php
//データベースの切断
$dbh = null;
?>

