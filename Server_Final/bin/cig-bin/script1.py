#!C:/Python34/
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

first = form.getvalue('first')
last  = form.getvalue('last')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>testing</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first, last))
print("</body>")
print("</html>")
