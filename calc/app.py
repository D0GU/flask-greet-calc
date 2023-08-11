from flask import Flask, request
import operations

app = Flask(__name__)


@app.route("/add")
def calc_add():
    return str(operations.add(int(request.args["a"]), int(request.args["b"])))


@app.route("/sub")
def calc_sub():
    return str(operations.sub(int(request.args["a"]), int(request.args["b"])))


@app.route("/mult")
def calc_mult():
    return str(operations.mult(int(request.args["a"]), int(request.args["b"])))


@app.route("/div")
def calc_div():
    return str(operations.div(int(request.args["a"]), int(request.args["b"])))
