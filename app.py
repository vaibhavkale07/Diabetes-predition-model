print("hello world")
# IMPORT STATEMENTS
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns

df = pd.read_csv("D:\diabites gui\diabetes.csv")

# HEADINGS
st.title('Diabetes Checkup')
st.sidebar.header('Patient Data')
st.subheader('Training Data Stats')
st.write(df.describe())
st.bar_chart(df)

x = df.drop(['Outcome'], axis = 1)
y = df.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 0)

def user_report():
   pregnancies = st.sidebar.slider('Pregnancies', 0,17, 3 )
   glucose = st.sidebar.slider('Glucose', 0,200, 120 )
   bp = st.sidebar.slider('Blood Pressure', 0,122, 70 )
   skinthickness = st.sidebar.slider('Skin Thickness', 0,100, 20 )
   insulin = st.sidebar.slider('Insulin', 0,846, 79 )
   bmi = st.sidebar.slider('BMI', 0,67, 20 )
   dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.0,2.4, 0.47 )
   age = st.sidebar.slider('Age', 21,88, 33 )


   user_report = {
      'pregnancies':pregnancies,
      'glucose':glucose,
      'bp':bp,
      'skinthickness':skinthickness,
      'insulin':insulin,
      'bmi':bmi,
      'dpf':dpf,
      'age':age
  }
   report_data = pd.DataFrame(user_report, index=[0])
   return report_data
    
#new_func()   
 
user_data = user_report()

rf =  RandomForestClassifier()
rf.fit(x_train , y_train)

st.subheader('Accuracy')
st.write(str(accuracy_score(y_test, rf.predict(x_test))*100)+'%')

user_result = rf.predict(user_data)
st.subheader('your Peport : ')
output = ''
if user_result[0]==0:
  output = ' wow!  you are healthy \n keep it up   '
else:
  output = 'you are not healthy \n please go to doctor'

st.write(output)