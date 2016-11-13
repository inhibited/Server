<?php
session_start();
$db = mysqli_connect("localhost","root","1234","authentication");
if(isset($_POST['register_btn'])){
	$username = mysqli_real_escape_string($db,$_POST['username']);
	$email = mysqli_real_escape_string($db,$_POST['email']);
	$password = mysqli_real_escape_string($db,$_POST['password']);
	$password2 = mysqli_real_escape_string($db,$_POST['password2']);
	if ($password == $password2) {
		$password = md5($password); //hash password before storing for security purposes
		$sql = "INSERT INTO users(username,email,password) VALUES('$username','$email','$password')";
		mysqli_query($db,$sql);
		$_SESSION['message'] = "You are now logged in";
		$_SESSION['username'] = $username;
		header("location: main.php"); //redirect to home page
	}
	else {
		$_SESSION['message'] = "The two passwords do not match";
	}
}
?> 
<!DOCTYPE html>
<html>
<head>
	<title>Register, login and logout user php mysql</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="header">
	<h1>Register or login to BACKDATED server</h1>
</div>
<?php
if (isset($_SESSION['message'])) {
	echo "<div id='error_msg'>".$_SESSION['message']."</div>";
	unset($_SESSION['message']);
}
?>
<form method="post" action="register.php">
	<table>
		<tr>
			<td>Username:</td>
			<td><input type="text" name="username" class="textInput" autocomplete="off"></td>
		</tr>
		<tr>
			<td>Email:</td>
			<td><input type="email" name="email" class="textInput" autocomplete="off"></td>
		</tr>
		<tr>
			<td>Password:</td>
			<td><input type="password" name="password" class="textInput"></td>
		</tr>
		<tr>
			<td>Password again:</td>
			<td><input type="password" name="password2" class="textInput"></td>
		</tr>
		<tr>
			<td>
				<input type="submit" name="register_btn" value="Register" >
			</td>
		</tr>
	</table>
</form>
<div style="text-align: center;font-size: 32px;padding-top: 64px">
	<button  onclick="window.location ='login.php'">Login</button>
</div>
</body>
</html>