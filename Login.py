#!C:\Users\SNEHASHISH\AppData\Local\Programs\Python\Python39\python.exe
import mysql.connector
import cgi
import os
connector = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "data"
)
cursor = connector.cursor()
sql = "SELECT * FROM signup"
cursor.execute(sql)
data = cursor.fetchall()

print("Content-type: text/html")
print("")

print("<html lang=\"en\">")
print("<head>")
print("\t" + "<meta charset=\"UTF-8\">")
print("\t" + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
print("\t" + "<title>Document</title>")
print("\t" + "<link rel=\"stylesheet\" href=\"new.css\">")
print("</head>")
print("<body>")
print("\t" + "<form  class = \"box\" action = \"\" methid = \"post\">")
print("\t\t" + "<h1>LOGIN</h1>")
print("\t\t" + "<input type = \"text\" name = \"\" placeholder = \"Username\">")
print("\t\t" + "<input type = \"password\" name = \"\" placeholder = \"Password\">")
print("\t\t" + "<input type = \"submit\" name =\"\" value = \"Login\">")
print("\t" + "</form>")
print("\t" + "")     
print("</body>")
print("</html")
for i in data:
    if i[0] and i[1]:
        print("Content-type: text/html")
        print("")
        print("<html lang=\"en\">")
        print("<head>")
        print("\t" + "<meta http-equiv = \"load\" content = 0; url = \"https://www.w3schools.com/howto/howto_js_redirect_webpage.asp\">")
        print("</head>")
        print("<body>")
        print("</body>")
        print("</html")
        