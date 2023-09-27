import time
from pathlib import Path
from datetime import datetime as dt


# print(pl)           # file path
# print(type(pl))     # file type
# print(pl.name)      # file fullname
# print(pl.stem)      # file name(only name)
# print(pl.suffix)    # file format like .pdf, .txt...


# p2 = Path('files')            # Get all path of files in selected folder
# print(list(p2.iterdir()))


def file_create(path_file, text_data, *data):
    time_now = dt.now()

    name_file = f"{time_now.year}_{time_now.month}_{time_now.day}_{time_now.hour}" \
                f"{time_now.minute}{time_now.second}{time_now.microsecond}"

    pl = Path(f'{path_file}/{name_file}.txt')

    list_files = []

    for i in (Path(path_file).iterdir()):
        list_files.append(i.name)

    if data[0] in list_files:
        with open(f'{path_file}/{data[0]}', 'a') as file:
            file.write(f"{text_data}\n")
            print(f'New data added to {data[0]} file')

    elif not pl.exists():
        with open(pl, 'w') as file:
            file.write(
                f'Hello.\n{name_file}.txt file is created and you can add new data!!!\n\n')
        with open(pl, 'a') as file:
            file.write(f"{text_data}\n")
            print(f'Created new file and added new data to {pl.name}')

    else:
        print("Something is wrong mr_sultonov_d")


file_create("files", "Assalomdan boshlanar kunimiz", '001.txt')
