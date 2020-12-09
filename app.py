from __future__ import division, print_function
# coding=utf-8
import os
import sys
import datetime
import glob


from keras.models import load_model, Model
import numpy as np
from scipy.misc import imread, imresize


# Flask utils
import flask
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = '/app/models/model-00020-0.19649-0.93514-0.45695-0.85000.h5'

gesture_class = ["Left Swipe", "Right Swipe", "Stop", "Thumbs Down", "Thumbs Up"]

def generator(folder_path):
    print('folder_path :', folder_path)
    img_idx = [0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 27, 28, 29]
    while True:

        batch_data = np.zeros((1, 18, 84, 84, 3))
        batch_labels = np.zeros((1, 5))
        imgs = os.listdir(folder_path)
        for idx, item in enumerate(img_idx):
            image = imread(folder_path + '/' + imgs[item]).astype(np.float32)
            if image.shape[1] == 160:
                image = imresize(image[:, 20:140, :], (84, 84)).astype(np.float32)
            else:
                image = imresize(image, (84, 84)).astype(np.float32)

            batch_data[0, idx, :, :, 0] = image[:, :, 0] - 104
            batch_data[0, idx, :, :, 1] = image[:, :, 1] - 117
            batch_data[0, idx, :, :, 2] = image[:, :, 2] - 123

        yield batch_data

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        all_files = flask.request.files.getlist("file[]")

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        del_dir = os.path.join(basepath, 'uploads')
        del_files = glob.glob(del_dir+"/*")
        if os.path.exists(del_dir):
            for df in del_files:
                os.remove(df)
        if not os.path.exists(del_dir):
            os.makedirs(del_dir)
        for f in all_files :
            file_path = os.path.join(
                basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)
        print("All Files Uploaded")
        test_generator = generator(del_dir)
        x = test_generator.__next__()
        print("x :", x.shape)
        # Load your trained model
        model = load_model(MODEL_PATH)
        model_func = Model(inputs=[model.input], outputs=[model.output])
        pred_idx = np.argmax(model_func.predict_on_batch(x), axis=1)
        print(" pred :", pred_idx)
        result = gesture_class[pred_idx[0]]
        return result


if __name__ == '__main__':
    #app.debug = True
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)

