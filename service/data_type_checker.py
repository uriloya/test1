# Uri Loya
from enums.file_type import FileType


def check_data_type(file_path: str) -> FileType:
    if 'jpg' in file_path:
        return FileType.IMAGE
    elif 'mp4' in file_path:
        return FileType.VIDEO
    else:
        print(f"Unsupported file!: {file_path}")
        return FileType.UNSUPPORTED
