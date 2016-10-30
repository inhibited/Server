#!/usr/bin/python3

import os
import html

def index():
	return """
<FORM value="form" action="dynamictest.get_info()" method="post">
  <P>
	<LABEL for="firstname">First Name: </LABEL>
	<INPUT type="text" name="firstname"><BR>
	<LABEL for="lastname">Last Name: </LABEL>
	<INPUT type="text" name="lastname"><BR>
	<LABEL for="email">email: </LABEL>
	<INPUT type="text" name="email"><BR>
	<INPUT type="radio" name="gender" value="Male">Male<BR>
	<INPUT type="radio" name="gender" value="Female">Female<BR>
	<INPUT type="submit" value="Send"> <INPUT type="reset">
  </P>
</FORM>
"""

def get_info(req):
	info = req.form
	first = info['firstname']
	last = info['lastname']
	email = info['email']
	gender = info['gender']
	return """
<h1>POST Method using mod_python</h1>
<hr>
Thanks for using our service:<br>
Your first name: %s <br>
Your last name: %s <br>
Your email address: %s <br>
Your gender: %s <br>
""" %(first, last.upper(), email, gender.lower())

def mthod():
	print("method working.")
	print(os.getcwd())

if __name__=='__main__':
	print("Wah!! Wah!!")
	print(index())
	mthod()

