import json
import os

import argparse
import shutil
from flask import Flask, request, render_template
import zipfile
from classifier import ImageClassifier

app = Flask(__name__)

classifier = ImageClassifier()


def zip_opener(file):
    with zipfile.ZipFile('./zip_data/zip_folders.zip', 'r') as zip_f:
        zip_f.extractall('./data')


@app.route('/', methods=['GET', 'POST'])
def upload_and_train():
    if request.method == 'POST':
        file = request.files['file']
        file.save('./zip_data/zip_folders.zip')
        zip_opener('./zip_data/zip_folders.zip')
        classifier.learn('./data')
        shutil.rmtree('./data/imgs')
        os.remove('./zip_data/zip_folders.zip')
        return render_template('success.html')

    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def pred_file():
    if request.method == 'POST':
        pic = request.files.get('file')
        pic.save('./data/pred.jpg')
        predict, simil, _, __ = classifier.predict('./data/pred.jpg')
        os.remove('./data/pred.jpg')
        return json.dumps({'predicted_value': predict, 'similarity_rate': simil})

    return render_template('pred.html')


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--host', nargs='?', default="0.0.0.0", type=str)
    parser.add_argument('--port', nargs='?', default=8000, type=int)

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_arguments()

    app.run(debug=False, host=args.host, port=args.port)
