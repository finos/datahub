from joblib import load
import numpy as np

class LinearRegressionModel:
    # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    def __init__(self, filename, xfields, yfields):
        self.model = load(filename)
        self.xfields = xfields
        self.yfields = yfields
        self.xvalues = []

    def set_precondition(self, data):
        self.xvalues = [[data[key] for key in self.xfields]]

    def make_one(self):
        predict_result = np.array(self.model.predict(self.xvalues))
        predict_result = predict_result[0]
        result = {}
        if not isinstance(predict_result, np.ndarray):
            # We need to make the row as an array in the case of single target y.
            predict_result = [predict_result]
        for column_name, column_value in zip(self.yfields, predict_result):
            result[column_name] = column_value

        return result
