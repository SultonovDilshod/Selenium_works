from pathlib import Path

rood_dir = Path('path_file_folder')
file_path = rood_dir.iterdir()
for i in file_path:
    new_name = "new-" + i.name
    new_file_path = i.with_name(new_name)
    print(new_file_path)
    i.rename(new_file_path)
