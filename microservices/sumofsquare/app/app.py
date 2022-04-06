from os import system
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class sumofsquare(Resource):
    def get(self, arg1, arg2):
        a= int(arg1)**2 + int(arg2)**2
        return a


api.add_resource(sumofsquare, '/sumofsquare/<arg1>&<arg2>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5053)
