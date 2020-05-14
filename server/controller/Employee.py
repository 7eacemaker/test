from flask_restful import Resource,Api, reqparse
from server.helper.predictionHelper import PredictorHelper

from webargs.flaskparser import use_args

from tablib import Dataset
from webargs import fields
import werkzeug
from server.helper.fileHelper import FileHelper

class Employee(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()

        employeesWithPrediction = FileHelper.loadExcelWithEmployeesAndDoingPrediction(args['file'])
        return {"prediction": employeesWithPrediction}