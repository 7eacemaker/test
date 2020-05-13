

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template
import requests
app = Flask(__name__)

#lectura del modelo (formato binario)
#model = pickle.load(open('model.pkl', 'r'))
#import torch
#model = torch.load('model.pkl')
with open('pickle_model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')

def home():
	return render_template("index.html")



# prediction function 
def ValuePredictor(to_predict_list): 
	to_predict = np.array(to_predict_list).reshape(1, 8) 
	#loaded_model = pickle.load(open("model.pkl", "rb")) 
	with open('pickle_model.pkl', 'rb') as file:
		loaded_model = pickle.load(file)
	
	result = loaded_model.predict(to_predict) 
	return result[0] 

@app.route('/result', methods = ['POST']) 
def result(): 
	if request.method == 'POST': 
		to_predict_list = request.form.to_dict() 
		to_predict_list = list(to_predict_list.values()) 
		to_predict_list = list(map(float, to_predict_list)) 
		result = ValuePredictor(to_predict_list)		 
		if int(result)== 1: 
			prediction ='El empleado va a dejar la empresa'
		else: 
			prediction ='El empleado no va a dejar la empresa'			
		return render_template("result.html", prediction = prediction) 

if __name__ == "__main__":
    app.run(debug=True)





