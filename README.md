# Scikit-learn-with-GUI
Easy to use interface for basic scikit-learn functions

## Introduction  
This project contains files for both front and back end python files for use with scikit-learn.  This is meant  
for anyone who wants to get into machine learning with python but does not know where to start. Hopefully by disecting  
this project you are able to understand the basic template of how machine learning and more specifically supervised learning 
works. This has applications for situations where pervious data is collected and is leveraged to predict what might occur 
in future cases with similar data. This GUI only supports the use of the Train/Test split method of supervised learning, but  contains 5 algorithms for different use cases.


## Technologies Used  
- Python 3.6  
- Scikit learn module for Python 3.6 (documentation: https://scikit-learn.org/stable/ )  
- WxPython module for Python 3.6 (documentation: https://wxpython.org/ )  
- Pandas module for Python 3.6 (documentaion: https://pandas.pydata.org/ )  

# Walkthrough   
1. Start by clicking the "Load Train Data" button circled in the picture below.  
![train_data](https://user-images.githubusercontent.com/52090139/71197494-bad54d00-225f-11ea-8d64-015bc5cd025c.JPG)  
    
2. Select ALL independent variables you would like to take into account when making the prediction  
![train_diag_box](https://user-images.githubusercontent.com/52090139/71199357-c88cd180-2263-11ea-86fa-0fbd4ea1045d.JPG)
  
3. Select which item you would like to predict for as shown below  

  
4. Click the drop down arrow as seen in the picutre below to select which model you would like to use to make a prediction  

  
5. Drag the slider to split up your data into training group and testing group. The number pointed to below is the percentage  
of data that will be used to train your data, and the remaining data will be used to test your prediction  

  
6. The results of your model will then be shown in the top right. Depending on what algorithm was selected, this will  
spit out different information. More than likely this will be in the from of a confusion matrix (How to read: https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/ )  

  
7. Click the "Select Prediction Data" button to pick another file with similar data in it to back test your model against.  
This will then pop up a dialog box as shown below and all of you predictions will be added into a new column in that file.
