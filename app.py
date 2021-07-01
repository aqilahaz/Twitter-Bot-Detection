from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
from retrieve_tweet import download_user
import joblib
import pandas as pd
import numpy as np
from analisis_data_profil import preprocess

app = Flask(__name__)

#pipe = joblib.load('model_new_2.pkl')
pipe = joblib.load('model_human_bot.pkl')

def prediction(df):
    pr = preprocess(df)
    pred = pipe.predict(pr)
    prediksi= ' '.join(pred)
    return prediksi

@app.route("/")
def index():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def handle_data():
    dl_user = request.form.get('chat_in')
    download_user(dl_user)
    return redirect(url_for('result'))
@app.route("/result/", methods=['POST','GET'])
def result():
    df = pd.read_csv('coba.csv')
    prediksi = prediction(df)
    filename = 'user.csv'
    data = pd.read_csv(filename, header=0)
    profile = list(data.values)
    for x in profile:
    	res=x[0]
    
    return render_template('result.html', profile=profile, res=res, prediksi=prediksi)

if __name__ == '__main__':
    app.run(debug=True)