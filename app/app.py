from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        myage = request.form['age']
        mysalary = request.form['salary']
        mymarital = request.form['marital']
        if str(myage) =='' or str(mysalary) =='' or str(marital) =='':
            return render_template('index.html', href2='Please insert your age salary and marital.')
        else:
            model = load('app/movie-prediction.joblib')
            np_arr = np.array([myage, mysalary, mymarital])
            predictions = model.predict([np_arr])  
            predictions_to_str = str(predictions)
            #return predictions_to_str
            return render_template('index.html', href2='The suitable movie for you (age:'+str(myage)+' ,salary:'+str(mysalary)+' ,marital:'+str(mymarital)+') is:'+predictions_to_str)
        

