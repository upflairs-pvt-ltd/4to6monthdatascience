from flask import Flask ,render_template,url_for,request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template("login.html")


@app.route("/logindata",methods=['GET','POST'])
def logindata():
    if request.method == "POST":
        name = request.form['name']
        e_mail = request.form['e_mail']
        password = request.form['password'] 
        userdata = {'name':name,'email':e_mail,'password':password}
        
        user_list = [{'name':'radhey','email':'ranjit.upflairs@gmail.com','password':"258"},
                        {'name':'anshika','email':'anshika.upflairs@gmail.com','password':"786"}]
        # redirect user to the profile page with name         
        return userdata 


if __name__ =="__main__":
    app.run(debug=True)