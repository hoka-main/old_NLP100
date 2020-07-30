<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>制作課題06-1</title>
</head>
<body>
<h1>
<?php
$photo[] = "./img/kuji1.png";
$photo[] = "./img/kuji2.png";
$photo[] = "./img/kuji3.png";
$photo[] = "./img/kuji4.png";
$photo[] = "./img/kuji5.png";
$num = count($photo);
$random = random_int(0, $num-1);
echo "<img src=" . $photo[$random] . ">";
echo "<br>"
?>
<a href="http://johodb.otemae.ac.jp/~zq16026s/">トップページに戻る</a>
</h1>
</body>
</html>