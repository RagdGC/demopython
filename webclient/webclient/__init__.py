from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = 'a76a5a10b7dd3ddf80988a0a71aee9f9'

@app.route('/')
def index():
    return render_template("index.html")

from . import empleados, estadojs, forms

app.register_blueprint(empleados.bp)
app.register_blueprint(estadojs.bp)
app.register_blueprint(forms.bp)