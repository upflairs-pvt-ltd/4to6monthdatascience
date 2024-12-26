import mysql.connector as mc 

conn = mc.connect(host="localhost",username="root",password="Radhey254875")

query1 = "create database flaskapp"
query2 = """create table contactdata 
(name varchar(30) , contact int , email varchar(50), subject varchar(60), message varchar(120))"""

try:
    myc = conn.cursor()   ## cursor object 
    myc.execute(query)
    print("Your database is created.")
except:
    print("Unable to create database!")

myc.close()
conn.close()