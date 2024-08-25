import pickle as pkl
from flask import Flask,render_template,redirect,request
import numpy as np

app = Flask(__name__)
with open('house.pkl','rb') as f:
    model = pkl.load(f)

@app.errorhandler(404)
def error_404(e):
    return render_template('error.html')

@app.route("/")
def new():
    return redirect('/home')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/submit",methods=['POST'])
def submit():
    #collecting data from webform
    sqft_living = float(request.form.get('sqft_living'))
    sqft_lot = float(request.form.get('sqft_lot'))
    sqft_above = float(request.form.get('sqft_above'))
    room = int(request.form.get('rooms'))
    array = np.array([[sqft_living,sqft_lot,sqft_above,room]])

    #predicting value
    price = model.predict(array)
    return render_template('output.html',prediction=price)
    



if __name__== "__main__":
    app.run(debug=True,port = 46)