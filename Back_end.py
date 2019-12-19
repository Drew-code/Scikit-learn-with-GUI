import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib



class logitmodel():
    def __init__(self, pandas_data_frame, y_variable, x_vars_as_list, test_size):
        self.data = pandas_data_frame

        self.independent = x_vars_as_list

        self.dependent = str(y_variable)

        self.test_size = test_size

        self.X = self.make_x_df(self.data, self.independent)

        self.y = self.data[self.dependent]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=(test_size/100), random_state=101)

        self.logmodel = LogisticRegression()

        self.logmodel.fit(self.X_train, self.y_train)

        self.predictions = self.logmodel.predict(self.X_test)

    def output_predict(self, data):
        predict_X = self.make_x_df(data, self.independent)
        predictions = self.logmodel.predict(predict_X)
        return predictions

    def save_model(self,model_name):
        pass





    def make_x_df(self, x_data, x_vars_as_list):

        x_df = pd.DataFrame()
        for x_var in x_vars_as_list:
            x_df[x_var] = x_data[x_var]

        return x_df


class linearmodel():
    def __init__(self, pandas_data_frame, y_variable, x_vars_as_list, test_size):
        self.data = pandas_data_frame

        self.independent = x_vars_as_list

        self.dependent = str(y_variable)

        self.test_size = test_size

        self.X = self.make_x_df(self.data, self.independent)

        self.y = self.data[self.dependent]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=(test_size/100), random_state=101)

        self.linmodel = LinearRegression()

        self.linmodel.fit(self.X_train, self.y_train)

        self.predictions = self.linmodel.predict(self.X_test)

    def output_predict(self, data):
        predict_X = self.make_x_df(data, self.independent)
        predictions = self.linmodel.predict(predict_X)
        return predictions



    def make_x_df(self, x_data, x_vars_as_list):

        x_df = pd.DataFrame()
        for x_var in x_vars_as_list:
            x_df[x_var] = x_data[x_var]

        return x_df

class KNN():
    def __init__(self, pandas_data_frame, y_variable, x_vars_as_list, test_size):
        self.data = pandas_data_frame

        self.independent = x_vars_as_list

        self.dependent = str(y_variable)

        self.test_size = test_size

        self.X = self.make_x_df(self.data, self.independent)

        self.y = self.data[self.dependent]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y,
                                                                                test_size=(test_size / 100),
                                                                                random_state=101)

        self.knn = KNeighborsClassifier(n_neighbors=1)

        self.knn.fit(self.X_train, self.y_train)

        self.predictions = self.knn.predict(self.X_test)

    def output_predict(self, data):
        predict_X = self.make_x_df(data, self.independent)
        predictions = self.knn.predict(predict_X)
        return predictions



    def make_x_df(self, x_data, x_vars_as_list):

        x_df = pd.DataFrame()
        for x_var in x_vars_as_list:
            x_df[x_var] = x_data[x_var]

        return x_df

class DecisionTree():
    def __init__(self, pandas_data_frame, y_variable, x_vars_as_list, test_size):
        self.data = pandas_data_frame

        self.independent = x_vars_as_list

        self.dependent = str(y_variable)

        self.test_size = test_size

        self.X = self.make_x_df(self.data, self.independent)

        self.y = self.data[self.dependent]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y,
                                                                                test_size=(test_size / 100),
                                                                                random_state=101)

        self.dtree = DecisionTreeClassifier()

        self.dtree.fit(self.X_train, self.y_train)

        self.predictions = self.dtree.predict(self.X_test)

    def output_predict(self, data):
        predict_X = self.make_x_df(data, self.independent)
        predictions = self.dtree.predict(predict_X)
        return predictions



    def make_x_df(self, x_data, x_vars_as_list):

        x_df = pd.DataFrame()
        for x_var in x_vars_as_list:
            x_df[x_var] = x_data[x_var]

        return x_df

class RandomForest():
    def __init__(self, pandas_data_frame, y_variable, x_vars_as_list, test_size):
        self.data = pandas_data_frame

        self.independent = x_vars_as_list

        self.dependent = str(y_variable)

        self.test_size = test_size

        self.X = self.make_x_df(self.data, self.independent)

        self.y = self.data[self.dependent]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y,
                                                                                test_size=(test_size / 100),
                                                                                random_state=101)

        self.rfc = RandomForestClassifier(n_estimators=100)

        self.rfc.fit(self.X_train, self.y_train)

        self.predictions = self.rfc.predict(self.X_test)

    def output_predict(self, data):
        predict_X = self.make_x_df(data, self.independent)
        predictions = self.rfc.predict(predict_X)
        return predictions



    def make_x_df(self, x_data, x_vars_as_list):

        x_df = pd.DataFrame()
        for x_var in x_vars_as_list:
            x_df[x_var] = x_data[x_var]

        return x_df




if __name__ == '__main__':
    MyApp()
    logitmodel()
    linearmodel()
    DecisionTree()
    KNN()
    RandomForestClassifier()

