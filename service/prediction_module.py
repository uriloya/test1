# Uri Loya
import numpy as np
from keras.models import model_from_json

from enums.animal_type import AnimalType


def predict_image(image) -> AnimalType:
    X = image_to_array(image)

    # Getting model:
    model_file = open('Data/Model/model.json', 'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)

    # Getting weights
    model.load_weights("Data/Model/weights.h5")
    Y = predict(model, X)
    print('It is a ' + Y.value + ' !')
    return Y


def image_to_array(image):
    X = np.zeros((1, 64, 64, 3), dtype='float64')
    X[0] = image
    return X


def predict(model, X) -> AnimalType:
    Y = model.predict(X)
    Y = np.argmax(Y, axis=1)
    Y = AnimalType.CAT if Y[0] == 0 else AnimalType.DOG
    return Y
