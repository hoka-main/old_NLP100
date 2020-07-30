<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>制作課題05-1</title>
</head>
<body>
<h1>
<?php
echo "初めてのPHP。<br>";
echo "PHPはスクリプト言語である<br>";
?>
<hr>
<?php
echo "<table>
<tr><td>5月1日</td><td>晴れ</td></tr>
<tr><td>5月2日</td><td>雨</td></tr>
<tr><td>5月3日</td><td>曇り</td></tr>
</table>";
?>
<hr>
<?php
echo "現在の時刻と日付は：";
echo date("Y/m/d H:i:s");
echo "です。<br>";
echo "一か月後の時刻と日付は：";
echo date("Y/m/d H:i:s", strtotime("+1 month"));
echo"です。<br>";
?>
<a href="http://johodb.otemae.ac.jp/~zq16026s/">トップページに戻る</a>

</h1>
</body>
</html>