from os import system
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class bitwiseand(Resource):
    def get(self, arg1, arg2):
        return int(arg1) & int(arg2)


api.add_resource(bitwiseand, '/and/<arg1>&<arg2>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5060)