from flask import Flask
from flask_restful import Resource,Api
from controller.Employee import Employee
from controller.Prediction import Prediction
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

api.add_resource(Prediction,'/prediction')
api.add_resource(Employee,'/employee')

CORS(app)


if __name__ == "__main__":
    app.run(debug=True)

