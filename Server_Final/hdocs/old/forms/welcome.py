import cgi

form = cgi.FieldStorage()
print("Welcome : ")
print(form['name'])
print(form)
