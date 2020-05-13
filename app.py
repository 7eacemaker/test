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
	return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

	int_features = [int(x) for x in request.form.values()]
	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)
	output = round(prediction[0],1)

	return render_template('index.html', prediction_text='Employee leave should be $ {}'.format(output))


  


def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)




