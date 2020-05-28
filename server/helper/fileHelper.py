import os
import pickle
from flask import jsonify
from tablib import Dataset
from helper.predictionHelper import PredictorHelper
import json

class FileHelper:
    @staticmethod
    def loadExcelWithEmployeesAndDoingPrediction(file):
        to_predict_list = []
        new_employees = []
        raw_data = file.read()
        imported_data = Dataset().load(raw_data, format='xlsx')
        employees = imported_data.export('json')
        employees_obj = json.loads(employees)

        for employee in employees_obj:
            to_predict_list.append(employee['satisfaction_level'])
            to_predict_list.append(employee['last_evaluation'])
            to_predict_list.append(employee['number_project'])
            to_predict_list.append(employee['average_montly_hours'])
            to_predict_list.append(employee['time_spend_company'])
            to_predict_list.append(employee['Work_accident'])
            to_predict_list.append(employee['promotion_last_5years'])
            to_predict_list.append(employee['salary'])

            if to_predict_list[0] != None:
                to_predict_list = list(map(float, to_predict_list))
                result = PredictorHelper.predictionValue(to_predict_list)[0]
                if int(result) == 1:
                    employee['predictionText']='El empleado va a dejar la empresa'
                    employee['probabilidad'] = str(PredictorHelper.predictionValue(to_predict_list)[1][1])
                else:
                    employee['predictionText']='El empleado no va a dejar la empresa'
                    employee['probabilidad'] = str(PredictorHelper.predictionValue(to_predict_list)[1][0])

                new_employees.append(employee)
                


            to_predict_list=[]

        return new_employees


