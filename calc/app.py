from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_request():
    """Handle GET request to add two numbers"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)

    return str(result)

@app.route('/sub')
def sub_request():
    """Handle GET request to subtract two numbers"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = sub(a, b)
    return str(result)

@app.route('/mult')
def mult_request():
    """Handle GET request to multiply two numbers"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = mult(a, b)
    return str(result)

@app.route('/div')
def div_request():
    """Handle GET request to divide two numbers"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = div(a, b)
    return str(result)

@app.route('/math/<operation>')
def do_math(operation):
    """Further study to shorten to amount of code needed for all operations"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    operation_functions = {"add": add(a, b), "sub": sub(a, b), "mult": mult(a,b), "div": div(a,b)}
    result = operation_functions[f"{operation}"]

    return str(result)