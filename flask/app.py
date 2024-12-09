# website (img,video,pdf)  <== static 
## static ==> publically available 

## templates  ==> webpages (html files)

from flask import Flask,render_template,render_template_string

app = Flask(__name__)   # __main__ 

@app.route('/')  # Home route 
def Home():
    # return "Hey Great job, This is HOME PAGE"
    return render_template("home.html")


@app.route('/about')  # http://127.0.0.1:5000/about
def about():
    job_designation = "Data Scientist"
    print(job_designation)
    return render_template('about.html')


@app.route("/contact")
def contact():
    print(job_designation)
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


if __name__ == "__main__":
    app.run(debug=True)  