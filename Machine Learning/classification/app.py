from flask import Flask , render_template , url_for ,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/application')
def application():
    return render_template('user_data.html') 

@app.route('/userdata',methods=['GET','POST'])
def userdata():
    if request.method == 'POST':
        gender = request.form['gender']  
        customer_type = request.form['customer_type']
        type_of_travel = request.form['typeoftravel']
        return f"you gender is : {gender} "


if __name__ == "__main__":
    app.run(debug=True)