<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>制作課題06-2</title>
</head>
<body>
<h1>
<?php
$day_numbers1 = "休日です";
$day_numbers2 = "平日です";
$day_numbers3 = "土曜日です";
$day_number = date('w');
if ($day_number <= 0){
echo "今日は".$day_numbers1;
}elseif($day_number >= 1 and $day_number <= 5){
echo "今日は".$day_numbers2;
}else{
echo "今日は".$day_numbers3;
}
echo "<br>"
?>
<a href="http://johodb.otemae.ac.jp/~zq16026s/">トップページに戻る</a>
</h1>
</body>
</html>