from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    nombre = "Andreé"
    licenciaturas = ["ISC","ID","ARQ"]
    return render_template('index.html',nombre = nombre, licenciaturas = licenciaturas,len=len(licenciaturas))