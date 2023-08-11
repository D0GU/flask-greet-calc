from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
@app.route('/welcome/<msg>')
def welcome(msg=""):
    if msg == "":
        return "welcome"
    else:
        return f"welcome {msg}"
