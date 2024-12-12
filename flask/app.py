# website (img,video,pdf)  <== static 
## static ==> publically available 

## templates  ==> webpages (html files)

from flask import Flask,render_template,render_template_string,session,url_for,request

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
        user_data = {"Name":name,"email":email,"contact":contact,"subject":subject,"message":message}
        print(user_data)
        return  user_data 


if __name__ == "__main__":
    app.run(debug=True)  