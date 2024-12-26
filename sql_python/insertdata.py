import mysql.connector as mc 

conn = mc.connect(host="localhost",username="root",password="Radhey254875",database="flaskapp")


query = """insert into contactdata (name,contact,email,subject,message)
           values ('anshika','9759194985','smart@gmail.com','welcome','hello how are you')"""

try:
    myc = conn.cursor()   ## cursor object 
    myc.execute(query)
    conn.commit()
    print("Your record has been sent into databse!")
except Exception as e :
    print("Unable to insert your data into database!",e)
    conn.rollback()

myc.close()
conn.close()