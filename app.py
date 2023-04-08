#!/usr/bin/env python
import cv2
import numpy as np
from flask_cors import CORS
from flask import Flask, request, jsonify

from inference import inference

app = Flask(__name__)
CORS(app)


@app.route("/test/")
def test():
    return "!!!! test flask app !!!!"




@app.route('/classify_exercise', methods=['POST'])
def classify_exercise():
    # Read image file and convert to RGB
    file = request.files['file']
    contents = file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    predicted_label, prediction_proba = inference(img)
    return jsonify(
        {
            "label": f"{predicted_label}",
            "proba": f"{prediction_proba}",
        }
    )



if __name__ == "__main__":
    app.run(debug=True)
