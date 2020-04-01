from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>我是首页!!!<h1>' 