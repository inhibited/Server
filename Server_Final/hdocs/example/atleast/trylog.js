	var uname = document.getElementById("username").value;
	var uid = document.getElementById("userid").value
	var pass = document.getElementById("password").value

	uname.addEventListener("blur", nameVerify, true);
	uid.addEventListener("blur", useridVerify, true);

	function Valid()
	{
		if(uname.value == "")
		{
			return false;
		}

		if(uid.value == "")
		{
			return false;
		}

		if (pass.value == "" ) 
		{
			return false;
		}
	}

	function nameVerify(){
		if (uname.value === "AZOAD") {
			return true;
		}
		else
		{
			return false;
			console.log("username not matched");
		}
	}

	function useridVerify(){
		if (uid.value != "") 
		{
			return true;
		}
	}

