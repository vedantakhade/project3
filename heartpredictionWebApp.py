import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load the heart disease dataset
df = pd.read_csv('import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load the heart disease dataset
df = pd.read_csv('heart.csv')

# Sidebar
st.sidebar.header('User Input Parameters')

def user_input_features():
    age = st.sidebar.slider('Age', 29, 77, 55)
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    cp = st.sidebar.slider('Chest Pain Type (cp)', 0, 3, 1)
    trestbps = st.sidebar.slider('Resting Blood Pressure (trestbps)', 94, 200, 125)
    chol = st.sidebar.slider('Serum Cholesterol (chol)', 126, 564, 250)
    fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', (0, 1))
    restecg = st.sidebar.slider('Resting Electrocardiographic Results (restecg)', 0, 2, 0)
    thalach = st.sidebar.slider('Maximum Heart Rate Achieved (thalach)', 71, 202, 150)
    exang = st.sidebar.selectbox('Exercise Induced Angina (exang)', (0, 1))
    oldpeak = st.sidebar.slider('ST Depression Induced by Exercise Relative to Rest (oldpeak)', 0.0, 6.2, 3.0)
    slope = st.sidebar.slider('Slope of the Peak Exercise ST Segment (slope)', 0, 2, 1)
    ca = st.sidebar.slider('Number of Major Vessels Colored by Fluoroscopy (ca)', 0, 4, 2)
    thal = st.sidebar.slider('Thalassemia (thal)', 0, 3, 2)
    
    data = {'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            'fbs': fbs,
            'restecg': restecg,
            'thalach': thalach,
            'exang': exang,
            'oldpeak': oldpeak,
            'slope': slope,
            'ca': ca,
            'thal': thal}
    
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('User Input parameters')
st.write(input_df)

# Load the saved RandomForestClassifier model
load_clf = pickle.load(open('heart_clf.pkl', 'rb'))

# Apply the model to make predictions
prediction = load_clf.predict(input_df)
prediction_proba = load_clf.predict_proba(input_df)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
')

# Sidebar
st.sidebar.header('User Input Parameters')

def user_input_features():
    age = st.sidebar.slider('Age', 29, 77, 55)
    sex = st.sidebar.selectbox('Sex', ('male', 'female'))
    cp = st.sidebar.slider('Chest Pain Type (cp)', 0, 3, 1)
    trestbps = st.sidebar.slider('Resting Blood Pressure (trestbps)', 94, 200, 125)
    chol = st.sidebar.slider('Serum Cholesterol (chol)', 126, 564, 250)
    fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl (fbs)', (0, 1))
    restecg = st.sidebar.slider('Resting Electrocardiographic Results (restecg)', 0, 2, 0)
    thalach = st.sidebar.slider('Maximum Heart Rate Achieved (thalach)', 71, 202, 150)
    exang = st.sidebar.selectbox('Exercise Induced Angina (exang)', (0, 1))
    oldpeak = st.sidebar.slider('ST Depression Induced by Exercise Relative to Rest (oldpeak)', 0.0, 6.2, 3.0)
    slope = st.sidebar.slider('Slope of the Peak Exercise ST Segment (slope)', 0, 2, 1)
    ca = st.sidebar.slider('Number of Major Vessels Colored by Fluoroscopy (ca)', 0, 4, 2)
    thal = st.sidebar.slider('Thalassemia (thal)', 0, 3, 2)
    
    data = {'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            'fbs': fbs,
            'restecg': restecg,
            'thalach': thalach,
            'exang': exang,
            'oldpeak': oldpeak,
            'slope': slope,
            'ca': ca,
            'thal': thal}
    
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('User Input parameters')
st.write(input_df)

# Load the saved RandomForestClassifier model
load_clf = pickle.load(open('heart_clf.pkl', 'rb'))

# Apply the model to make predictions
prediction = load_clf.predict(input_df)
prediction_proba = load_clf.predict_proba(input_df)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
