# configuration
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/root/static')
app.config["SECRET_KEY"] = "RjizqbyGDxHpCRZ0z3QgeW"
app.config['UPLOAD_FOLDER'] = './root/Upload'

app.config['DEBUG'] = True

# homepage
@app.route("/")
def homepage():
    return render_template('index.html')