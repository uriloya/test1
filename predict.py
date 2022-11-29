# Arda Mavi & Uri Loya
import asyncio
import sys

from service import prediction_module, data_type_checker, video_handler
from enums.file_type import FileType
from get_dataset import get_img, get_corrected_img_array


def main():
    file_path = sys.argv[1]

    # check type of file in order to choose the right processor
    file_type = data_type_checker.check_data_type(file_path)

    if file_type == FileType.IMAGE:
        img = get_img(file_path)
        sync_prediction(img)
    elif file_type == FileType.VIDEO:
        video_frames_list = video_handler.extract_video_frames(file_path)

        loop = asyncio.get_event_loop()
        coros = [async_prediction(frame, count) for count, frame in enumerate(video_frames_list)]
        loop.run_until_complete(asyncio.gather(*coros))
        loop.close()
    else:
        print("And error has occurred!")


def sync_prediction(img):
    prediction_module.predict_image(img)


async def async_prediction(frame, count: int):
    if frame is None:
        return
    img = get_corrected_img_array(frame)
    animal_type = prediction_module.predict_image(img)
    await video_handler.write_frame_to_file(frame, animal_type, count)


if __name__ == '__main__':
    main()
