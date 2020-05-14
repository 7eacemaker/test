from webargs import fields

predictionRequest = {
    'satisfaction_level': fields.Integer(
        required=True
    ),
    'last_evaluation': fields.Integer(
        required=True
    ),
    'number_project': fields.Integer(
        required=True
    ),
    'average_montly_hours': fields.Integer(
        required=True
    ),
    'time_spend_company': fields.Integer(
        required=True
    ),
    'Work_accident': fields.Integer(
        required=True
    ),
    'promotion_last_5years': fields.Integer(
        required=True
    ),
    'salary': fields.Integer(
        required=True
    ),
}