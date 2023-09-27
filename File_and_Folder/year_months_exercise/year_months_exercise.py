from pathlib import Path


def answer_by_me():
    root_dir = Path('files')

    for path in root_dir.glob("*"):
        for i in path.glob("**/*"):
            if i.is_file():
                year, month = i.parts[1], i.parts[2]
                new_name = year + "-" + month + "-" + i.name
                new_path = i.with_name(new_name)
                i.rename(new_path)


def answer_by_video_lesson():
    root_dir = Path('files')

    for path in root_dir.glob("**/*"):
        if path.is_file():
            sub_folders = path.parts[1:-1]
            new_name = "-".join(sub_folders) + path.name
            new_path = path.with_name(new_name)
            path.rename(new_path)


