# Deployment Script With Flask
import pickle
from flask import Flask, request

app = Flask(__name__)

with open("model/np_model.pkl", "rb") as f:
    np_model = pickle.load(f)

with open("model/df_model.pkl", "rb") as f:
    df_model = pickle.load(f)


@app.route("/")
def index():
    return {
        "status": "SUCCESS",
        "message": "Hello World",
        "code": 200
    }, 200

# Predict Route for Numpy Model


# http://localhost:5000/predict/np?sl=2&sw=1.5&pl=1.0&pw=0.7
@app.route("/predict/np")
def predict_np():
    args = request.args
    sl = args.get("sl", default=0.0, type=float)  # Sepal Length
    sw = args.get("sw", default=0.0, type=float)  # Sepal Width
    pl = args.get("pl", default=0.0, type=float)  # Petal Length
    pw = args.get("pw", default=0.0, type=float)  # Petal Width

    new_data = [[sl, sw, pl, pw]]
    predict = np_model.predict(new_data)
    iris_class = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    return {
        "status": "SUCCESS",
        "model": "Numpy Model",
        "input": {
            "sepal length": sl,
            "sepal width": sw,
            "petal length": pl,
            "petal wwidth": pw
        },
        "message": "Prediction Successful",
        "result": int(predict[0]),
        "class": iris_class[predict[0]],
        "code": 200
    }, 200


# http://localhost:5000/predict/df?sl=1.2&sw=3.0&pl=1.0&pw=2.0
@app.route("/predict/df")
def predict_df():
    args = request.args
    sl = args.get("sl", default=0.0, type=float)  # Sepal Length
    sw = args.get("sw", default=0.0, type=float)  # Sepal Width
    pl = args.get("pl", default=0.0, type=float)  # Petal Length
    pw = args.get("pw", default=0.0, type=float)  # Petal Width

    new_data = [[sl, sw, pl, pw]]
    predict = df_model.predict(new_data)
    iris_class = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    return {
        "status": "SUCCESS",
        "model": "DataFrame Model",
        "input": {
            "sepal length": sl,
            "sepal width": sw,
            "petal length": pl,
            "petal wwidth": pw
        },
        "message": "Prediction Successful",
        "result": int(predict[0]),
        "class": iris_class[predict[0]],
        "code": 200
    }, 200


app.run(debug=True)
