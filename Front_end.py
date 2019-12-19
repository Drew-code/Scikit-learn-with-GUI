import wx

import wx.lib.agw.labelbook as LB

import subprocess
import pandas as pd
import Back_end as be

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.externals import joblib

#creating the main window
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title='EzPredict', size=(600, 900))

        self.model = None
        self.panel = Modeling(self)







class Visualize(wx.Panel):
    def __init__(self, parent):
        super(Visualize, self).__init__(parent)




class Modeling(wx.Panel):
    def __init__(self, parent):
        super(Modeling, self).__init__(parent)

        self.parent = parent



        #LOAD DATA BUTTONs
        self.LoadxData = wx.Button(self,label = 'Load Train Data',size=(100,25))
        self.LoadxData.Bind(wx.EVT_BUTTON,self.OnLoadTrain)

        self.butn_run = wx.Button(self, label='Run', pos=(250, 50))
        self.butn_run.Bind(wx.EVT_BUTTON, self.on_run)

        #prediction button
        self.butn = wx.Button(self, label='Select Prediction Data',pos = (225,350))
        self.butn.Bind(wx.EVT_BUTTON, self.on_predict)




        self.data = pd.DataFrame()





        self.xvariablesLabel = wx.StaticText(self,label = 'Select Independant Variables')
        self.Select_xVariables = wx.ListBox(self,size= (200,300),style = wx.LB_MULTIPLE,choices = [])
        #self.Select_xVariables.Bind(wx.EVT_LISTBOX, self.StoreXVar)


        #Select Test variables
        self.yvariablesLabel = wx.StaticText(self, label='Dependant Variable')
        self.Select_yVariables = wx.ListBox(self, size=(200, 100), choices=[])
        #self.Select_yVariables.Bind(wx.EVT_LISTBOX, self.StoreYVar)

        #Pick Model Type
        self.pick_model_label = wx.StaticText(self, label='Model Type')
        self.model_choice = wx.Choice(parent=self, choices=['Linear Regression',
                                                             'Logistic Regression','K-Nearest Neighbors',
                                                             'Decision Tree','Random Forest'])



        #Pick Split ration
        self.split_title = wx.StaticText(self,label='Data Split')
        self.split_data = wx.Slider(self, value=0,
                                    minValue=0.0,
                                    maxValue=100,
                                    style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS,
                                    size=(200, 50))
        self.split_data.Bind(wx.EVT_SLIDER, self.OnSlide)

        self.display_results_title = wx.StaticText(self, label='Model Accuracy', pos=(375, 55))
        self.model_display_box = wx.StaticText(self, label='Results will show here', pos=(300, 80))





          # SIZER CREATION
        main_sizer = wx.BoxSizer(wx.VERTICAL)



        xData_sizer = wx.BoxSizer(wx.HORIZONTAL)

        xvariable_sizer = wx.BoxSizer(wx.HORIZONTAL)
        xvariablebox_sizer = wx.BoxSizer(wx.HORIZONTAL)

        yvariable_sizer = wx.BoxSizer(wx.HORIZONTAL)
        yvariablebox_sizer = wx.BoxSizer(wx.HORIZONTAL)

        model_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        choices_sizer = wx.BoxSizer(wx.HORIZONTAL)

        split_title_sizer = wx.BoxSizer(wx.HORIZONTAL)
        split_data_sizer = wx.BoxSizer(wx.HORIZONTAL)

        btn_run_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # ADDING EVERYTHING TO THE SIZERS



        xData_sizer.Add(self.LoadxData, 0, wx.ALL, 5)


        xvariable_sizer.Add(self.xvariablesLabel, 0, wx.ALL, 5)
        xvariablebox_sizer.Add(self.Select_xVariables, 0, wx.ALL, 5)

        yvariable_sizer.Add(self.yvariablesLabel, 0, wx.ALL, 5)
        yvariablebox_sizer.Add(self.Select_yVariables, 0, wx.ALL, 5)

        model_label_sizer.Add(self.pick_model_label, 0, wx.ALL, 5)
        choices_sizer.Add(self.model_choice, 0, wx.ALL, 5)

        split_title_sizer.Add(self.split_title,0,wx.ALL,5)
        split_data_sizer.Add(self.split_data,0,wx.ALL | wx.EXPAND,5)

        btn_run_sizer.Add(self.butn_run,0,wx.ALL,5)




        # adding sizers to main sizer

        main_sizer.Add(xData_sizer, 0, wx.ALL, 5)
        main_sizer.Add(xvariable_sizer, 0, wx.ALL, 5)
        main_sizer.Add(xvariablebox_sizer, 0, wx.ALL, 5)
        main_sizer.Add(yvariable_sizer, 0, wx.ALL, 5)
        main_sizer.Add(yvariablebox_sizer, 0, wx.ALL, 5)
        main_sizer.Add(model_label_sizer, 0, wx.ALL, 5)
        main_sizer.Add(choices_sizer, 0, wx.ALL, 5)
        main_sizer.Add(split_title_sizer,0,wx.ALL,5)
        main_sizer.Add(split_data_sizer,0, wx.ALL, 5)
        main_sizer.Add(btn_run_sizer,0,wx.ALL,5)



        self.SetSizer(main_sizer)



    #LOAD DATA FUNCTIONALITY
    def OnLoadTrain(self,event):
        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Open CSV file", wildcard="(*.csv)|*.csv",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                pass  # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            self.factor = pd.read_csv(pathname)
            factors = pd.DataFrame(self.factor)
            self.variables = list(factors.columns.values)
            self.Select_xVariables.Append(self.variables)
            self.Select_yVariables.Append(self.variables)





    def on_predict(self, event):
        with wx.FileDialog(self, "Open CSV file", wildcard="(*.csv)|*.csv",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                pass  # the user changed their mind

            pathname = fileDialog.GetPath()
            self.data = pd.read_csv(pathname)
            predictions = self.parent.model.output_predict(self.data)

            prediction_results = pd.read_csv(pathname,error_bad_lines=False)
            prediction_results = pd.DataFrame(prediction_results)
            prediction_results['Predictions'] = predictions
            prediction_results.to_csv(pathname, index=False)

            wx.MessageBox('Your File Has Been Updated With Predictions', 'Prediction Complete'
                                                                        ,style =wx.OK | wx.ICON_INFORMATION)


            return predictions




    #storing split data for train test split
    def OnSlide(self, event):
        value = self.split_data.GetValue()
        return(value)

    #storing xvariables in list
    def StoreXVar(self,event):
        xvars = []

        xvar_indexes = list(self.Select_xVariables.GetSelections())

        #print(xvars)

        for i in xvar_indexes:
            xvars.append(self.Select_xVariables.GetString(i))

        return xvars


    #storing Y variable
    def StoreYVar(self,event):


        # i'm assuming this is always one selection
        yvar = str(self.Select_yVariables.GetStringSelection())

        #print(yvar)
        return yvar

    def SelectAll(self, event):

        pass



    def Modeltype(self,event):

        model_type = self.model_choice.GetStringSelection()
        return model_type

    def on_run(self, event):


        type = self.Modeltype('event')

        y_var = self.StoreYVar('event')

        x_vars = self.StoreXVar('event')

        split_value = self.OnSlide('event')

        if y_var in x_vars:
            wx.MessageBox('Please remove ' + y_var +' from independant variables selection','Over Lapping Variables'
                                                                                         ,style =wx.OK | wx.ICON_INFORMATION)





        else:

            if type == 'Logistic Regression':

                model = be.logitmodel(self.factor, y_var, x_vars, split_value)
                self.model_display_box.SetLabelText(classification_report(model.y_test, model.predictions))
                self.parent.model = model



            if type == 'Linear Regression':
                model = be.linearmodel(self.factor, y_var, x_vars, split_value)

                self.model_display_box.SetLabelText("Mean Absolute Error: "+str(metrics.mean_absolute_error(model.y_test, model.predictions))+'\nMean Squared Error: '+ str(metrics.mean_squared_error(model.y_test, model.predictions))+ '\nMean Error: ' + str((np.sqrt(metrics.mean_squared_error(model.y_test, model.predictions)))))
                print(metrics.mean_squared_error(model.y_test, model.predictions))
                print(np.sqrt(metrics.mean_squared_error(model.y_test, model.predictions)))
                self.parent.model = model

            if type == 'K-Nearest Neighbors':
                model = be.KNN(self.factor, y_var, x_vars, split_value)
                self.model_display_box.SetLabelText(classification_report(model.y_test, model.predictions))
                self.parent.model = model


            if type == 'Decision Tree':
                model = be.DecisionTree(self.factor, y_var, x_vars, split_value)
                self.model_display_box.SetLabelText(classification_report(model.y_test, model.predictions))
                self.parent.model = model


            if type == 'Random Forest':
                model = be.RandomForest(self.factor, y_var, x_vars, split_value)
                self.model_display_box.SetLabelText(classification_report(model.y_test, model.predictions))
                self.parent.model = model













class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None,title='First Window')
        self.frame.Show()
        return True
#running the app
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()


