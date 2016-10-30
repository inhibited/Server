<?php
session_start();
?>
<!DOCTYPE html>
<html>
<head>
	<title>login_main</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<h1 class="header">Login Successful</h1>
<h2 style="text-align: center">Welcome back ! <?php echo $_SESSION['username']; ?></h2>
<div><button onclick="window.location='logout.php'">Logout</button></div>
</body>
</html>