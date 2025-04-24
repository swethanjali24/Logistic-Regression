

# Loading the important libraries for streamlit app
import streamlit as st
import numpy as np
import pickle

# Loading the model
with open ('Logistic_Regression.pkl','rb') as f:
    model = pickle.load(f)

# Streamlit interface
st.title('Species Predictor')
st.write('🌸This app uses Logistic regression model to predict the type of species based on the given features🌸')

# Collects the user input

Sepal_Length=st.number_input('Enter the Sepal length in cm')
Sepal_Width=st.number_input('Enter the Sepal width in cm')
Petal_Length=st.number_input('Enter the Petal length in cm')
Petal_Width=st.number_input('Enter the Petal width in cm')

# Button to predict

if st.button('Predict the type of Species'):
    input_data=np.array([[Sepal_Length,Sepal_Width,Petal_Length,Petal_Width]])

   # Prediction
    prediction=model.predict(input_data)

    if prediction==0:
        st.success('The predicted species is Setosa')
    elif prediction==1:
        st.success('The predicted species is Versicolor')
    else:
        st.success('The predicted species is Virginica')