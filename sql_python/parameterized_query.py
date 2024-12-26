import mysql.connector as mc 

conn = mc.connect(host="localhost",username="root",password="Radhey254875",database="flaskapp")

# parameterized query 
parameterized_query = """insert into contactdata (name,contact,email,subject,message)
           values (%s,%s,%s,%s,%s)"""

data = ("Radhey","854569857","jiradhey@gmail.com","Good bye","where are you from")
try:
    myc = conn.cursor()   ## cursor object 
    myc.execute(parameterized_query,data)
    conn.commit()
    print("Your record has been sent into databse!")
except Exception as e :
    print("Unable to insert your data into database!",e)
    conn.rollback()

myc.close()
conn.close()