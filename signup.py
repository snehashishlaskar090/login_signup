#!C:\Users\SNEHASHISH\AppData\Local\Programs\Python\Python39\python.exe
import cgi
import cgitb
import mysql.connector

form = cgi.FieldStorage()
username = form.getvalue("username")
pw = form.getvalue("pw")

sq = mysql.connector.connect(
    host = "localhost",
    username ="root",
    password = "",
    database = "data"
)
cursor = sq.cursor()
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
print("\t" + "<form  class = \"box\" action = \"signup.py\" method = \"post\">")
print("\t\t" + "<h1>SIGN UP</h1>")
print("\t\t" + "<input type = \"text\" name = \"username\" placeholder = \"Create a Username\">")
print("\t\t" + "<input type = \"password\" name = \"pw\" placeholder = \"Create a Password\">")
print("\t\t" + "<input type = \"submit\" name =\"\" value = \"sign up\">")
print("\t" + "</form>")
print("\t" + "")
print("</body>")
print("</html")
sql = "INSERT INTO signup (username, password) VALUES (%s, %s)"
vql = (username,pw)
cursor.execute(sql, vql)
sq.commit()


        

