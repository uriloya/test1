# Arda Mavi

import sys
from keras.models import Sequential
from keras.models import model_from_json

import data_type_checker
import video_converter
from file_types import FileType
from get_dataset import get_img
import numpy as np


def image_to_array(image_path: str):
    img = get_img(image_path)
    X = np.zeros((1, 64, 64, 3), dtype='float64')
    X[0] = img
    return X


def predict_image(X):
    # Getting model:
    model_file = open('Data/Model/model.json', 'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)

    # Getting weights
    model.load_weights("Data/Model/weights.h5")
    Y = predict(model, X)
    print('It is a ' + Y + ' !')


def predict(model, X):
    Y = model.predict(X)
    Y = np.argmax(Y, axis=1)
    Y = 'cat' if Y[0] == 0 else 'dog'
    return Y


if __name__ == '__main__':
    video_converter.test_video()

    file_path = sys.argv[1]
    file_type = data_type_checker.check_data_type(file_path)

    if file_type == FileType.IMAGE:
        X = image_to_array(file_path)
        predict_image(X)
    elif file_type == FileType.VIDEO:

        video_frames = []
        for frame in video_frames:
            X = image_to_array(file_path)
            predict_image(X)
    else:
        print("And error has occured!")
