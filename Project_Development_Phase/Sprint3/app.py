import numpy as np
from flask import Flask,jsonify,request,render_template
import pickle

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def Home():
    return render_template('Manual_predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    float_features=[float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    prediction = model.predict(features)
    return render_template("Manual_predict.html", prediction_text = "Car Fuel Consumption(L/100km) : {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
