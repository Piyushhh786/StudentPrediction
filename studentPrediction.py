import numpy as np
import pandas as pd
import pickle


def load_model():
        with open("student_lr_final_model.pkl",'rb') as file:
                model,scaler,label = pickle.load(file)
        return model,scaler,label
def preprocessing_input_data(data,scaler,le):
        # print(data)
        if(data['Extracurricular Activities']=='No') :
                data['Extracurricular Activities'] = 0
        else : data['Extracurricular Activities'] = 1
        df = pd.DataFrame([data])
        df_transformed = scaler.transform(df)
        return df_transformed
def predict_data(data):
        model,scaler,le = load_model()
        transformed_data = preprocessing_input_data(data,scaler,le)
        prediction = model.predict(transformed_data)
        return prediction


#----------------api part-------------------------------------
from flask import Flask, request as req, jsonify as json 
from flask_cors import CORS

# making flask api for our nextJs application
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
        return "Hello World"

@app.route("/predict",methods = ["POST"])
def predict():
        data = req.get_json()
        print(data)
        features = data.get("features")
        if not features:
                return json({"error": "Missing 'features' key in request body"}), 400
        # print(f"data: {features}")
        prediction = predict_data(features)
        print(f"pridiction: {prediction}")
        return json({"prediction":prediction.tolist()})

if __name__ == "__main__": # this ensures the file.py will not run indirectly from other script
        app.run(debug=True)