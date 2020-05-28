
from flask_restful import Resource,Api
from helper.predictionHelper import PredictorHelper
from webargs.flaskparser import use_args
from webargs import fields

class Prediction(Resource):
    predictionRequest = {
     
        'Work_accident': fields.Integer(
            required=True
        ),
        'time_spend_company': fields.Integer(
            required=True
        ),
        'salary': fields.Integer(
            required=True
        ),
        'number_project': fields.Integer(
            required=True
        ),
        'satisfaction_level': fields.Integer(
            required=True
        ),
        'last_evaluation': fields.Integer(
            required=True
        ),
        'average_montly_hours': fields.Integer(
            required=True
        ),
        'promotion_last_5years': fields.Integer(
            required=True
        ),
    }
    def get(self):
        return {}

    @use_args(predictionRequest)
    def post(self,request):
        to_predict_list = []
        for key in request:
            to_predict_list.append(request[key])

        to_predict_list = list(map(float, to_predict_list))
        result = PredictorHelper.predictionValue(to_predict_list)[0]
        print(result)

        if int(result) == 1:
            return {'messageResult': 'El empleado va a dejar la empresa','predictionResult': result}
        return {'messageResult': 'El empleado no va a dejar la empresa','predictionResult': result}





