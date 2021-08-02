from flask import Flask, render_template, request
import pickle
import numpy as np
model = pickle.load(open('loan_status.pkl', 'rb'))  # opening pickle file in read mode
app = Flask(__name__)  # initializing Flask app
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        d1 = request.form['Married']
        if (d1 == 'No'):
            d1 = 0
        else:
            d1 = 1
        d2 = request.form['Gender']
        if (d2 == 'Male'):
            d2 = 1
        else:
            d2 = 0
        d3 = request.form['Education']
        if (d3 == 'Graduate'):
            d3 = 1
        else:
            d3 = 0
        d4 = request.form['Self_Employed']
        if (d4 == 'No'):
            d4 = 0
        else:
            d4 = 1
        d5 = request.form['ApplicantIncome']
        d6 = request.form['CoapplicantIncome']
        d7 = request.form['LoanAmount']
        d8 = request.form['Loan_Amount_Term']
        d9 = request.form['Credit_History']
        if (d9 == 'All debts paid'):
            d9 = 1
        else:
            d9 = 0
        d10 = request.form['Property_Area']
        if (d10 == 'Urban'):
            d10 = 2
        elif (d10 == 'Rural'):
            d10 = 0
        else:
            d10 = 1
        d11 = request.form['Dependents']
        if (d11 == '3+'):
            d11 = 3
        elif (d11=='2'):
            d11 = 2
        elif (d11=='1'):
            d11 = 1
        else:
            d11 = 0
        arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9,d10,d11]])
        pred = model.predict(arr)
        if pred == 0:
            return render_template('index.html', prediction_text="Sorry! You are not eligible for Loan.")
        else:
            return render_template('index.html', prediction_text="Congrats! You are eligible for Loan.")
        return render_template('index.html')
app.run(host="0.0.0.0")            # deploy
#app.run(debug=True)                # run on local system