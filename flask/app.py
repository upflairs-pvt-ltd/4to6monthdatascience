# website (img,video,pdf)  <== static 
## static ==> publically available 

## templates  ==> webpages (html files)

from flask import Flask,render_template,render_template_string,session,url_for,request
import mysql.connector as mc 
conn = mc.connect(host="localhost",username="root",password="Radhey254875",database="flaskapp")
query = """insert into contactdata (name,contact,email,subject,message)
           values (%s,%s,%s,%s,%s)"""


app = Flask(__name__)   # __main__ 
app.secret_key = "dkfd4343"

# session = dict()  # {}   
# session['name'] = 'radhey'
@app.route('/')  # Home route 
def Home():
    # return "Hey Great job, This is HOME PAGE"
    return render_template("home.html")


@app.route('/about')  # http://127.0.0.1:5000/about
def about():
    session["job_designation"] = "Data Scientist"
    return render_template('about.html')


@app.route("/contact")
def contact():
    # print(session['job_designation'])
    return render_template('contact.html') 


@app.route('/service')
def service():
    message = """
    <html> 
    <head>
    <title> Testing </title>
    <body>
    <h1> Hey this SERvice page</h1>
    </body>
    </html>
    """
    return render_template_string(message)
    # return message
    # return "Hello this is service page!"
    # return render_template('contact.html') 


@app.route("/userdata",methods=['GET','POST'])
def userdata():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        subject = request.form['subject']
        message = request.form['message']
        contact_detail = (name,contact,email,subject,message)

        try:
            myc = conn.cursor()   ## cursor object 
            myc.execute(query,contact_detail)
            conn.commit()
            print("Your record has been sent into databse!")
        except Exception as e :
            print("Unable to insert your data into database!",e)
            conn.rollback()

        myc.close()
        conn.close()
        return  "Your record has been sent into databse!"

# backend ===>   frontend 
@app.route('/dashbord')
def dashbord():

    data = {"Name":"Radhey","age":27,"address":"mathura"}
    subjects = ['math','physics','chemistry','science']
    query = "select * from contactdata"
    try:
        myc = conn.cursor()   ## cursor object 
        myc.execute(query)
        data_from_database = myc.fetchall()
        print("Your record has been sent into databse!")
    except Exception as e :
        print("Unable to insert your data into database!",e)
        

    myc.close()
    conn.close()
    return render_template('dashboard.html',userdata=data,sub=subjects,database=data_from_database)



if __name__ == "__main__":
    app.run(debug=True)  