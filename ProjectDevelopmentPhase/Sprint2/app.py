import numpy as np
from flask import Flask,jsonify,request,render_template
import pickle

app = Flask(__name__, template_folder='templates')
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def predict():
    return render_template('Manual_predict.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    x_test=[[float(x) for x in request.form.values()]]
    print('actual',x_test)
    pred=model.predict(x_test)
    return render_template("Manual_predict.html", prediction_text = ("Car Fuel Consumption(L/100km) : {}",pred[0]))
if __name__ == "__main__":
    app.run(debug=True)