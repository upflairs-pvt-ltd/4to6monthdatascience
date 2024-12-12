from flask import Flask , render_template ,redirect,url_for 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")




@app.route("/pass_student/<name>/<int:score>")
def pass_student(name,score):
    output = f"This is {name} and score is : {score}"
    return output 


@app.route("/fail_student/<name>/<int:score>")
def fail_student(name,score):
    output = f"This is {name} and score is : {score}"
    return output 


@app.route('/result/<name>/<int:score>')  # dynamic url 
def result(name,score):
    status = ""
    if score > 50: 
        status = "pass"
    else:
        status = "fail"

    status = status + "_student"  # pass_student 
    return redirect(url_for(status,name=name,score=score)) 



if __name__ == "__main__":
    app.run(debug=True)