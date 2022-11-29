import cv2
import numpy as np
from scipy.misc import imresize

import predict


def test_video():
    cap = cv2.VideoCapture('Data/Videos/cats_and_dogs.mp4')

    while(cap.isOpened()):
        # print("in loop")
        ret, frame = cap.read()
        img_size = 64
        frame2 = imresize(frame, (img_size, img_size, 3))
        X = np.zeros((1, 64, 64, 3), dtype='float64')
        X[0] = frame2
        predict.predict_image(X)
        try:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except Exception as e:
            print(f"error: {e}")
            break

    print("done loop")
    cap.release()
    cv2.destroyAllWindows()
