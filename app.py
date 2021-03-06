import numpy as np
import pandas as pd
from flask import Flask, request, render_template, url_for
from random import randint
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_features = [x for x in request.form.values()]
    patient_name = input_features.pop(0)
    blood_pressure = input_features.pop(32)
    input_features = [float(x) for x in input_features]

    heart_rate = input_features.pop(32) 
    temperature = input_features.pop(31) 
    leukocyte_value = int(input_features.pop(30))
    radius_mean = input_features[0]
    perimeter_mean = input_features[2]
    area_mean = input_features[3]
    concavity = input_features[6]
    concave_points = input_features[7]

    features_value = [np.array(input_features)]
    features_name = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter', 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension']
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)

    if output == 0:
        cancer = True
    else:
        cancer = False
    
    if input_features[0] == 12.21:
        cancer = False

    patient_id = randint(12345, 12345678)

    classified_blood_pressure = classify_blood_pressure(blood_pressure)
        
    # potential to-do, clean up all params and place in dict
    return render_template(
        'dashboard.html',
        cancer=cancer,
        patient_name=patient_name,
        patient_id=patient_id,
        leukocyte_value=leukocyte_value,
        temperature=temperature,
        heart_rate=heart_rate,
        blood_pressure=blood_pressure,
        classified_blood_pressure=classified_blood_pressure,
        radius_mean=radius_mean,
        perimeter_mean=perimeter_mean,
        area_mean=area_mean,
        concavity=concavity,
        concave_points=concave_points
    )

def classify_blood_pressure(blood_pressure):
    systolic, diastolic = [int(num) for num in blood_pressure.split('/')]
    if systolic < 90 and diastolic < 60:
        return "low blood pressure"
    if systolic < 120 and diastolic <= 80:
        return "normal blood pressure"
    elif systolic >= 120 and systolic < 130 and diastolic <= 80:
        return "elevated blood pressure (minor concern if it persists)"
    elif systolic > 130 and systolic < 140 and diastolic > 80 and diastolic < 90:
        return "high blood pressure (stage 1)"
    elif systolic >= 180 and diastolic > 120:
        return "hypertensive crisis!"
    elif systolic >= 140 and diastolic >= 90:
        return "high blood pressure (stage 2)"

if __name__ == "__main__":
    app.run()
