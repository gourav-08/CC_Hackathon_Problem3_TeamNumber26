from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Resource
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


''' class Add(Resource):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def get() '''


def add(n1, n2):
    print(n1, '-', type(n1))
    return int(n1)+int(n2)


def minus(n1, n2):
    return int(n1)-int(n2)


def multiply(n1, n2):
    return int(n1)*int(n2)


def divide(n1, n2):
    if n2 == "0":
        return 'Division by Zero exception'
    return int(n1)/int(n2)


@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        result = requests.get('http://addition:5059/add/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == 'minus':
        result = requests.get('http://minus:5058/minus/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == 'multiply':
        result = requests.get('http://multiply:5057/multiply/' +
                              str(number_1) + '&' + str(number_2)).text
    elif operation == 'divide':
        result = requests.get('http://divide:5056/divide/' +
                              str(number_1) + '&' + str(number_2)).text
    elif operation == "bitwiseand":
        result = requests.get('http://bitwiseand:5060/and/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == "sumofsquare":
        result = requests.get('http://sumofsquare:5053/sumofsquare/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == "average":
        result = requests.get('http://average:5052/average/' +
                              str(number_1)+'&'+str(number_2)).text
    elif operation == "modulus":
        result = requests.get('http://modulus:5051/modulus/' +
                              str(number_1)+'&'+str(number_2)).text
    flash(
        f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
