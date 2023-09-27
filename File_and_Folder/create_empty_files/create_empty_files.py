from pathlib import Path
import zipfile as zf


def create_new_files():
    root_dir = Path('files')

    for i in list(range(11, 23)):
        file_name = str(i) + ".txt"
        file_path = root_dir / Path(file_name)
        file_path.touch()


def create_new_zip_files():
    root_dir = Path('files')
    archive_root = root_dir / Path('archived.zip')

    with zf.ZipFile(archive_root, 'w') as zipped:
        for path in root_dir.rglob('*.txt'):
            zipped.write(path)
            path.unlink()  # If you write unlink() code, txt will be deleted


def extract_zip_file():
    root_dir = Path('zip_files')
    destination_path = Path('zip_files/Natija')

    for path in root_dir.rglob('*.zip'):
        with zf.ZipFile(path, 'r') as zipped:
            final_path = destination_path / Path(path.stem)
            zipped.extractall(path=final_path)


def absolute(a, b):
    """
    :param a: '21.txt'
    :param b: 'absolute 22.txt'
    :return: nothing
    """
    for i in [a, b]:
        print(Path(f'files/{i}').absolute())


def search_absolute(search):
    path = Path('files')

    for i in path.glob('*.txt'):
        if i.is_file():
            if str(search) in i.name:
                print(i.absolute())


def move_files_to_another_folder():
    root_dir = Path('files')
    for path in root_dir.glob('*.txt'):
        with open(path, 'wb') as file:
            file.write(b'Dilshod new text')
        # path.unlink()

