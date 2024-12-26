import mysql.connector as mc 

conn = mc.connect(host="localhost",username="root",password="Radhey254875")

if conn.is_connected():
    print("Your connection is successfully established!")
else:
    print("unable to connect with your database!")

conn.close()