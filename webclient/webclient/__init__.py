from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

from . import empleados, estadojs

app.register_blueprint(empleados.bp)
app.register_blueprint(estadojs.bp)