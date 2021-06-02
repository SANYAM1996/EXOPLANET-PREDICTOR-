# import the Required library
from flask import Flask, render_template, request
import pickle
import sklearn.externals
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
# computation of planets.pkl is the model file used for the deployment
mul_reg = open("Computation of planets.pkl", "rb")
ml_model = joblib.load(mul_reg)

@app.route("/")
def home():
    return render_template('home.html')
# adding the parameters of model
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    print("")
    if request.method == 'POST':
        print(request.form.get('discoverymethod'))
        try:
            default_flag = int(request.form['default_flag'])
            sy_snum = int(request.form['sy_snum'])
            discoverymethod = int(request.form['discoverymethod'])
            pl_orbper = float(request.form['pl_orbper'])
            pl_orbsmax = float(request.form['pl_orbsmax'])
            pl_msinie = float(request.form['pl_msinie'])
            pl_orbeccen = float(request.form['pl_orbeccen'])
            st_teff = float(request.form['st_teff'])
            st_rad = float(request.form['st_rad'])
            st_mass = float(request.form['st_mass'])
            st_logg = float(request.form['st_logg'])
            sy_dist = float(request.form['sy_dist'])




            pred_args = [default_flag, sy_snum, discoverymethod, pl_orbper, pl_orbsmax, pl_msinie,pl_orbeccen,st_teff,st_rad,st_mass,st_logg,sy_dist]
            pred_args_arr = np.array(pred_args)
            pred_args_arr = pred_args_arr.reshape(1, -1)
            
            model_prediction = ml_model.predict(pred_args_arr)
            model_prediction = round(int(model_prediction), 2)
        except ValueError:
            return "Please check if the values are entered correctly"
    return render_template('predict.html', prediction = model_prediction)


if __name__ == "__main__":
    app.run(debug=True)
#app.run(host = '0.0.0.0',port=8080) uncomment this line while deployment