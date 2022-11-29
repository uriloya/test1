# Uri Loya
from file_types import FileType


def check_data_type(file_path: str) -> FileType:
    if file_path.find('jpg'):
        return FileType.IMAGE
    elif file_path.find('mp4'):
        return FileType.VIDEO
    else:
        print(f"Unsupported file!: {file_path}")
        return FileType.UNSUPPORTED
