from peewee import *
from models import *
from flask import Flask, render_template, request
from main import list_evil

app = Flask(__name__)

@app.route('/')
def index():
    for i in list_evil:
        Evil.create(name=i)
    return render_template('index.html', ev=list_evil)

if __name__ == '__main__':
    app.run(debug=True)
