from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/',methods=['GET'])
def Home():
	return render_template('page.html')

@app.route("/predict",methods=['POST'])
def predict():
	if request.method == 'POST':
		ram = int(request.form['ram'])
		disp = float(request.form['display'])
		bat = int(request.form['battery'])

		pred = model.predict([[ram,disp,bat]])
		return render_template('page.html',prediction_texts=f"Price is {pred}")
	else:
		return render_template('page.html')

if __name__ == "__main__":
	app.run(debug=True)