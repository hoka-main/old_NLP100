<?php
//データベースの接続
require_once "./dbconnect.php";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Blog</title>
</head>
<body>
<?php
//エラー処理
if(!isset($_POST["title"]) or !isset($_POST["body"])){
    exit("<p>未送信<br><a href=admin.php>管理ページ</a></p>");
}elseif(empty($_POST["title"]) or empty($_POST["body"])){
    exit("<p>未入力<br><a href=admin.php>管理ページ</a></p>");
}

//受け取った値を変数に格納   
$title= htmlspecialchars($_POST["title"], ENT_QUOTES);
$body = nl2br(htmlspecialchars($_POST["body"], ENT_QUOTES));
//SQLの実行
try {
    $sql = "INSERT INTO blog (title,body) VALUES (:title,:body)";
    $sth = $dbh->prepare($sql);
    $sth->bindParam(":title", $title, PDO::PARAM_STR);
    $sth->bindParam(":body", $body, PDO::PARAM_STR);
    $sth->execute();
    //画像ファイルのファイル名を決めるために登録したレコード No を取得する
    $lastno = $dbh->lastInsertId(); //最後に登録された no を取得する関数
    //もし、ファイルアップロードがあれば、ファイル名を変更してサーバーに格納する
    //第 7 回資料を参照
    if (is_uploaded_file($_FILES["upfile"]["tmp_name"])) {
        $filename = "./img/" .$lastno. ".jpg"; //ファイル名の確定
    if (move_uploaded_file($_FILES["upfile"]["tmp_name"],$filename)) {
        chmod($filename,0644); //ファイルのアクセス権を設定する
    }
}
//データベースの切断
$dbh = null;
//リダイレクト（自動的に指定したファイルにジャンプする）
header("Location: ./admin.php");
	
} catch(Exception $e) {
	echo ("Error:" . $e->getMessage());
}

?>
</body>
</html>
<?php

?>
