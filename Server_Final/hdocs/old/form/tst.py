#!/usr/bin/python3


import cgi
import cgitb;

cgitb.enable()

print("Content-Type: text/html")
print()                          

form = cgi.FieldStorage()

def POST():
	
