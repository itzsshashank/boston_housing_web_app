# Importing Flask essentials
from flask import Flask, request, render_template, redirect, url_for

# Importing Pandas for Data Reading
import pandas as pd

# Importing Numpy for Array Manipulation
import numpy as np

# Importing own modules
# from py_modules import data_extraction as de

# Import pickle module to load models
import pickle

# Flask App
ml_app = Flask(__name__)


# Boston House Price Predictor
@ml_app.route('/boston_house_price_predictor', methods = ['POST', 'GET'])
def boston_house_price_predictor():

	if request.method == "POST":
		# Getting Input Data from UI
		'LSTAT', 'RM', 'PTRATIO', 'INDUS', 'TAX', 'NOX'
		lstat = float(request.form['lstat'])
		rm = float(request.form['rm'])
		ptratio = float(request.form['ptratio'])
		indus = float(request.form['indus'])
		tax = float(request.form['tax'])
		nox = float(request.form['nox'])

		# Forming an input array
		input_array = [[lstat, rm, ptratio, indus, tax, nox]]

		# Loading Loan Status Predictor Model
		boston_house_price_predictor = pickle.load(open('C:\\Users\\shash\\Desktop\\NEW BAI\\Machine-Learning-Projects\\models\\boston_house_price_predictor.pkl', 'rb'))

		# Prediction
		price_predicted = np.round(boston_house_price_predictor.predict(input_array), 2)

		# Predicting Probability
		# predict_proba = boston_house_price_predictor.predict_proba(input_array) * 100
		return render_template('boston_house_price_predictor.html',
                	        price_predicted = price_predicted,
                	        input_array = input_array, n=5)
	return render_template('boston_house_price_predictor.html', n=5)


# App Launcher
if __name__ == '__main__':
	ml_app.run(debug = True, port = 3000)