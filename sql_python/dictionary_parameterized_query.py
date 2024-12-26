import mysql.connector as mc 

conn = mc.connect(host="localhost",username="root",password="Radhey254875",database="flaskapp")

# dictionary parameterized query 
dictionary_parameterized_query = """insert into contactdata (name,contact,email,subject,message)
           values (%(name)s,%(contact)s,%(email)s,%(subject)s,%(message)s)"""

data = {"name":"Rahul","contact":"7415256325","email":"rahul@gmail.com","subject":"Hii","message":"hello"}
try:
    myc = conn.cursor()   ## cursor object 
    myc.execute(dictionary_parameterized_query,data)
    conn.commit()
    print("Your record has been sent into databse!")
except Exception as e :
    print("Unable to insert your data into database!",e)
    conn.rollback()

myc.close()
conn.close()