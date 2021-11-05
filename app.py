from flask import Flask, render_template, request, redirect, url_for, abort
import requests
import joblib

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

# route untuk memasukkan data rumah yang dicari
@app.route('/post', methods=['POST'])
def cari():
    Kecamatan = int(request.form['Kecamatan'])
    Daerah = int(request.form['Daerah'])
    kamar_tidur = int(request.form['kamar_tidur'])
    luas_bangunan = int(request.form['luas_bangunan'])
    luas_lahan = int(request.form['luas_lahan'])
    harga = round(model.predict([[Kecamatan, Daerah, kamar_tidur, luas_bangunan, luas_lahan]])[0], 2)
    return redirect(url_for('hasil', harga=harga))

# route untuk menampilkan hasil perhitungan
@app.route('/hasil/<int:harga>')
def hasil(harga):
    return render_template('hasil.html', harga=harga)

# route untuk menampilkan halaman error
@app.errorhandler(404)
def error(error):
    return render_template('error.html')

if __name__ == "__main__":
    # model diimport menggunakan package joblib
    model = joblib.load('model.sav',"rb")
    app.run(debug=True)