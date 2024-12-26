import mysql.connector as mc 

conn = mc.connect(host="localhost",username="root",password="Radhey254875",database="flaskapp")


query = """create table contactdata 
(name varchar(30) , contact varchar(14) , email varchar(50), subject varchar(60), message varchar(120))"""

try:
    myc = conn.cursor()   ## cursor object 
    myc.execute(query)
    conn.commit()
    print("Your Table is created.")
except Exception as e :
    print("Unable to create Table : ",e)
    conn.rollback()

myc.close()
conn.close()