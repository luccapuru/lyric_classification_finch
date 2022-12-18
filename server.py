from flask import Flask, request, jsonify
import pred_utils
from flask_cors import CORS



app = Flask(__name__)
rf = pred_utils.open_model("models/rf_model.pkl")
lr = pred_utils.open_model("models/lr_model.pkl")
svc = pred_utils.open_model("models/svc_model.pkl")
CORS(app)


@app.route('/classification', methods=["POST", "GET"])
def predict():
    try:
        text = request.args.get("lyric")
        # text = request.form

        print(text)

        response = {"svm": pred_utils.make_prediction(svc, text),
                    "logistic_regression": pred_utils.make_prediction(lr, text),
                    "random_forest": pred_utils.make_prediction(rf, text)}
        # response = {"LosgisticRegression":pred_utils.make_prediction(lr, text),
        # "RandomForest":pred_utils.make_prediction(rf, text)}

        return jsonify(response)
    except Exception as e:
        print(e)


app.run(host="0.0.0.0", port=81)
