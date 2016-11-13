<?php
session_start();
?>
<!DOCTYPE html>
<html>
<head>
	<title>registered</title>
</head>
<body>
<h1 style="text-align: center;color: green">You have successfully registered to <div style="color: Blue">BACKDATED</div>server</h1>
<h2 style="text-align: center">Welcome <?php echo $_SESSION['username']; ?></h2>
<h2>PLease login to continue </h2>
<button onclick="window.location ='login.php'">Login</button>
</body>
</html>