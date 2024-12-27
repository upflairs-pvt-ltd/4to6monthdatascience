import mysql.connector as mc 

user_creditions  = {"host":"localhost","username":"root","password":"Radhey254875","database":"flaskapp"}
conn = mc.connect(**user_creditions)
# if conn.is_connected():
#     print('yes')
# else:
#     print("no")

query = "select * from contactdata"
try:
    myc = conn.cursor(buffered=True)
    myc.execute(query)
 
    rows = myc.fetchmany(2)
    print(rows)
    print("successfully fetched data from database!") 

except Exception as e:
    print("Unable to fetch data from database! : ",e) 

myc.close()
conn.close()