from pathlib import Path
from datetime import datetime as dt


def answer_by_mr_sultonov():
    path = Path("files")
    stats = path.stat()
    date_created = dt.fromtimestamp(stats.st_ctime)
    date_created_str = date_created.strftime("%Y-%m-%d_%H-%M-%S")

    file_paths = path.glob("**/*")
    for i in file_paths:
        if i.is_file():
            new_name = f"{date_created_str}-{i.name}"
            new_path = i.with_name(new_name)
            i.rename(new_path)


def answer_by_video_lesson():
    rood_dir = Path("files")
    for path in rood_dir.glob("**/*"):
        if path.is_file():
            create_date = dt.fromtimestamp(path.stat().st_ctime)
            create_date_str = create_date.strftime("%Y-%m-%d_%H-%M-%S")
            new_filename = create_date_str + "-" + path.name
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)
