# Uri Loya

from typing import List

import cv2
import imageio

from animal_types import AnimalType


def extract_video_frames(video_path) -> List:
    # note that this method is limited to system RAM, it might be better to do it one by one
    video_frames_list = []
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        unused, frame = cap.read()
        video_frames_list.append(frame)
        try:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except:
            break

    cap.release()
    cv2.destroyAllWindows()

    return video_frames_list


def write_frame_to_file(frame, animal_type, count):
    if animal_type == AnimalType.CAT:
        imageio.imwrite(f"output/cats/{count}.jpg", frame)
    elif animal_type == AnimalType.DOG:
        imageio.imwrite(f"output/dogs/{count}.jpg", frame)
    else:
        print("Unsupported type!")
