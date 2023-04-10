#!/usr/bin/env python
import cv2
import argparse
import numpy as np

from flask_cors import CORS
from flask import Flask, request, jsonify

from inference import inference

app = Flask(__name__)
CORS(app)


@app.route("/test")
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


parser = argparse.ArgumentParser()
parser.add_argument('--url', help='ACCESS LINK', default=None)
parser.add_argument('--port', help='PORT NUM', default=None)

args = parser.parse_args()

if __name__ == "__main__":
    if args.url:
        for rule in list(app.url_map.iter_rules())[1:]:
                print(str(args.url)+str(rule))
        print('\n')
    
    app.run(debug=True, port=args.port)