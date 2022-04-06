from os import system
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class divide(Resource):
    def get(self, arg1, arg2):
        if arg2 == '0':
            return "Exception: Division by Zero"
        return float(arg1)/float(arg2)


api.add_resource(divide, '/divide/<arg1>&<arg2>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5056)
