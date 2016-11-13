
function validate() {
	var username = document.getElementById("username").value;
	var userid = document.getElementById("userid").value;
	var password = document.getElementById("password").value;
	if ( username == "AZOAD" && userid == "cseku" && password == "12345")
	{
		alert ("Login successfully");
		window.location = "main.html";
		return false;
	else
	{
		alert("unmatched information");
		return false;
	}
}