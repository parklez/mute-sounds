import os
import shutil
from settings import PATH_TO_BACKUP, PATH_TO_HL, EXCLUDE_DIRS


PATH_TO_SILENT_WAV = os.path.join(PATH_TO_HL, 'valve', 'sound', 'ambience', '_comma.wav')
CSTRIKE_PATH = os.path.join(PATH_TO_HL, 'cstrike_downloads', 'sound')


def retrieve_files(path: str, exclude: list) -> list:
    files_list = []
    for root, dirs, files in os.walk(path, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if file.endswith('.wav'):
                entry = os.path.join(root, file)
                files_list.append(entry)
    return files_list

def replace_sound(sound: bytes, dest: str):
    with open(dest, 'wb') as arquivo:
        arquivo.write(sound)

def make_zip(base_dir: str, output: str, file_format='zip'):
    """Create zip file

    Args:
        base_dir (str): path to dir to be archived
        output (str): path to file to be created
        format (str, optional): format to be used. Defaults to 'zip'.
    """
    shutil.make_archive(base_name=output,
                        format=file_format,
                        base_dir=base_dir)


if __name__ == "__main__":
    SILENT_WAV = open(PATH_TO_SILENT_WAV, 'rb').read()

    # 1. Make backup if PATH_TO_BACKUP is set
    if PATH_TO_BACKUP:
        make_zip(CSTRIKE_PATH, PATH_TO_BACKUP)
    # 2. Iterate over and replace file by file
    for file in retrieve_files(CSTRIKE_PATH, EXCLUDE_DIRS):
        replace_sound(SILENT_WAV, file)

    #SILENT_WAV.close()
    # 3. Done!
    print('Done! :)')
