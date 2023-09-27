from pathlib import Path


def way_of_me():
    list_months = []

    for i in list(Path('months_path_folder').iterdir()):
        list_months.append(i.name)

    for month in list_months:
        rood_dir = Path(f'months_path_folder/{month}')
        file_path = rood_dir.iterdir()
        for i in file_path:
            new_name = month + "-" + i.name
            new_file_path = i.with_name(new_name)
            print(new_file_path)
            i.rename(new_file_path)


def video_lesson():
    root_dir = Path('months_path_folder')
    file_paths = root_dir.glob("**/*")
    # print(list(file_paths))

    for path in file_paths:
        # print(path)
        if path.is_file():
            # print(path)
            patent_folder = path.parts[-2]
            # print(patent_folder)
            new_name = patent_folder + "-" + path.name
            # print(new_name)
            new_path = path.with_name(new_name)
            path.rename(new_path)
