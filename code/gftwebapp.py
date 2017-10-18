from flask import Flask, render_template
from GliderFlightTest.code.exam import Exam

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

