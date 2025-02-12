from flask import Flask , render_template , url_for ,request
import joblib 
model = joblib.load("logistic_regrssion.lb")

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
        gender = int(request.form['gender'])  
        customer_type = int(request.form['customer_type'])
        type_of_travel = int(request.form['typeoftravel'])
        flight_class = str(request.form['flight_class'])
        age = int(request.form['age'])
        flight_distance = int(request.form['flight_distance'])
        flght_enterment = int(request.form['flght_enterment'])
        bagage_handling = int(request.form['bagage_handling'])
        cleaning = int(request.form['cleaning'])
        deprtr_delay = int(request.form['deprtr_delay'])
        arival_delay = int(request.form['arival_delay'])


        Class_Eco =0
        Class_Eco_Plus=0
        if flight_class == "0":
            # economy class 
            Class_Eco = 1 
            Class_Eco_Plus = 0 
        
        elif flight_class == "1":
            #economy plus 
            Class_Eco = 0 
            Class_Eco_Plus = 1 
        else:
            # bussiness 
            Class_Eco = 0 
            Class_Eco_Plus = 0  

        unseen_data_points = [[gender,customer_type,type_of_travel,
                        Class_Eco, Class_Eco_Plus,age,flight_distance,flght_enterment,
                        bagage_handling,cleaning,deprtr_delay,arival_delay]]

        output = model.predict(unseen_data_points)[0]
        if output  == 0:
            return f"passer is not satisfied"
        else:
            print("Passenger is satisfied")

if __name__ == "__main__":
    app.run(debug=True)