from flask import *
import joblib
model = joblib.load('loanstatus.joblib')
app = Flask(__name__) 
  

@app.route('/static/assets')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)
# Default route added using a decorator, for view function 'welcome' 
# We pass a simple string to the frontend browser 
@app.route('/') 
def welcome(): 
    return render_template('index.html')

@app.route('/predic') 
def datacollectio(): 
    return render_template('data.html')


@app.route('/status',methods=[ 'POST']) 
def loanstatus(): 
    try:
        if request.method == 'POST':
            Gender = request.form['gender']
            Marrage = request.form['Marrage']
            Self_Employed = request.form['Self_Employed']
            ApplicantIncome = request.form['ApplicantIncome']
            CoapplicantIncome = request.form['CoapplicantIncome']
            LoanAmount = request.form['LoanAmount']
            Dependents = request.form['Dependents']
            Education = request.form['Education']
            Property_Area = request.form['Property_Area']
            Credit_History = request.form['Credit_History']
            Loan_Amount_Term = request.form['Loan_Amount_Term']
    except:
        return render_template('error.html')
    prediction = model.predict([[Gender,Marrage,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
    # data = request.get_json()
    print("jjsj",prediction)
    status = str(prediction)
    if status[1] == '0':
        return render_template('status.html',value=False)
    elif status[1] == '1':
        return render_template('status.html',value=True)

    
     
  
  
# Start with flask web app, with debug as True,# only if this is the starting page 
if(__name__ == "__main__"): 
    app.run(debug=True)