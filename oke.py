from crypt import methods
from operator import index
from wsgiref.validate import validators
from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

# import re
# import nltk
# import pymysql.cursors
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# # nltk.download("vader_lexicon")
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# # Open database connection
# db = pymysql.connect("localhost","testuser","test123","TESTDB" )
# # prepare a cursor object using cursor() method
# cursor = db.cursor()
# # execute SQL query using execute() method.
# cursor.execute("SELECT * FROM datalabel")
# disconnect from server
# db.close()

app = Flask(__name__, static_url_path="")
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    File = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload")

@app.route('/', methods=["GET", "POST"])
def main():
#     if request.method == "GET":
#         return render_template('index.html')
#     elif request.method == "POST":
#         print(request.form.get("upload"))
#         return
    return render_template('index.html')

@app.route('/upload', methods=["GET", "POST"])
def main():
    # form = UploadFileForm()
    # if form.validate_on_submit():
    #     file = form.file.data
    #     file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
    # return render_template('index.html', form = form)

    #   if request.method == "POST":
    #     return render_template('upload.html')
    # elif request.method == "POST":
    #     csv_file = request.files.get("file")
    #     X_test = pd.read_csv(csv_file, index_col="PassengerId")
    #     return X_test.to_html()

@app.route('/data')
def main():
    return render_template('index2.html')

@app.route('/hasil')
def main():
    return render_template('index3.html')


if __name__=="__main__":
    
    app.run(debug = True)

# @app.route('/upload' methods=['GET','POST'])
# def upload():
#     data = pd.read_csv('datalabelled-coba.csv', header=None)
#     return render_template("index.html")

# @app.route('/tampil' methods=['POST'])
# def data():
#     data[1].dropna()
#     return render_template("")

# def hapusurl(text):
#     return re.sub(r'https\S+', '', text)

# def removeusername(text):
#     pattern = r'[@]\w+'
#     text = re.sub(pattern, '', text)
#     return text

# def removehastag(text):
#     pattern = r'[#]\w+'
#     text = re.sub(pattern, '', text)
#     return text

# def hapuskurung(text):
#     pattern = r'[^a-zA-Z0-9\s]'
#     text = re.sub(pattern, '', text)
#     return text

# def clean_data(text):
#     text = hapusurl(text)
#     text = removeusername(text)
#     text = removehastag(text)
#     text = hapuskurung(text)
#     return text

# # =============================

# def tokenize(text):
#     text = word_tokenize(text)
#     return text

# def stopword(text):
#     return [word for word in text if word not in list_stopwords]

# def clean_data2(text):
#     text = tokenize(text)
#     text = stopword(text)
#     return text

# # ================================

# # def stemming(text):
# #     factory = StemmerFactory()
# #     stemmer = factory.create_stemmer()
# #     return [stemmer.stem(word) for word in text]

# # def clean_data3(text):
# #     text = stemming(text)
# #     return text

# # data['clean3']= data['clean2'].apply(clean_data3)

# # =========================
# def clean_data_testing(text):
#     text = hapusurl(text)
#     text = removeusername(text)
#     text = removehastag(text)
#     text = hapuskurung(text)
#     text = stopword(text)
#     return text

# return render_template("tampildata.html")

