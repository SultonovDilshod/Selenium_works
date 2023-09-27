from pathlib import Path


def answer_for_extension_mr_sultonov():
    dirs = Path('files')
    for i in dirs.glob('*'):
        new_name = f"{i.stem}.txt"
        new_path = i.with_name(new_name)
        i.rename(new_path)


def answer_for_extension_by_video_lesson():
    root_dir = Path('files')
    for i in root_dir.rglob('*.txt'):
        # rglob('*.txt') <==> glob('**/*.txt')
        if i.is_file():
            new_name = i.with_suffix('.csv')
            i.rename(new_name)
