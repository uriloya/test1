# Arda Mavi & Uri Loya
import asyncio
import sys
from keras.models import model_from_json

import data_type_checker
import video_converter
from animal_types import AnimalType
from file_types import FileType
from get_dataset import get_img, get_corrected_img_array
import numpy as np


def main():
    file_path = sys.argv[1]

    # check type of file in order to choose the right processor
    file_type = data_type_checker.check_data_type(file_path)

    if file_type == FileType.IMAGE:
        img = get_img(file_path)
        predict_image(img)
    elif file_type == FileType.VIDEO:
        video_frames_list = video_converter.extract_video_frames(file_path)

        loop = asyncio.get_event_loop()
        coros = [async_prediction(frame, count) for count, frame in enumerate(video_frames_list)]
        loop.run_until_complete(asyncio.gather(*coros))
        loop.close()
    else:
        print("And error has occurred!")


async def async_prediction(frame, count):
    if frame is None:
        return
    img = get_corrected_img_array(frame)
    animal_type = predict_image(img)
    await video_converter.write_frame_to_file(frame, animal_type, count)


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
    Y = AnimalType.DOG if Y[0] == 0 else AnimalType.CAT
    return Y


if __name__ == '__main__':
    main()
