import numpy as np
import os
import pickle

class PredictorHelper:
    @staticmethod
    def loadModelFile():
        os.chdir(os.path.dirname(__file__))
        file_path = str(os.getcwd()) + '/dataModel/linux/1pickle_model.pkl'
        print(file_path)
        with open(file_path, 'rb') as file:
            loaded_model = pickle.load(file)
        return loaded_model

    @staticmethod
    def predictionValue(to_predict_list):
        to_predict = np.array(to_predict_list).reshape(1, 8)    
        model_loaded = PredictorHelper.loadModelFile()
        result = model_loaded.predict(to_predict)
        prob = model_loaded.predict_proba(to_predict)
        return result[0], prob[0]





