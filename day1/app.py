from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '我是day1里面的首页'