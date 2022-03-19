from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
app = Flask(__name__)
ml_model = open("Logistic_model.pkl", "rb")
model = joblib.load(ml_model)

# @app.route('/test')
# def test():
#     return "Using Flask for this Webpage"


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.form.get('MMSE'))
        try:
            MMSE = float(request.form['MMSE'])
            eTIV = float(request.form['eTIV'])
            nWBV = float(request.form['nWBV'])
            ASF = float(request.form['ASF'])
            # Creating a dataframe using all the values
            row_df = pd.DataFrame([pd.Series([MMSE, eTIV, nWBV, ASF])])
            print(row_df)
            prediction = model.predict(row_df)  # Predicting the output
            prediction = int(prediction)
            print(print)
        except ValueError:
            return "please check that you have entered correct values"
    return render_template('predict.html', predicting=prediction)


if __name__ == '__main__':
    app.run(debug=True)
