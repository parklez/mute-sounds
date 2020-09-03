"""
Task:
    - Scan directories recursively for .wav files and return a list

Possible solutions:
    - os.walk(path) & file.endswith(.wav)
    - pathlib.Path(path).rglob('*.wav')
    - glob.glob(path, recursive=True)
    - os.walk(path) & fnmatch.filter(files, '*.wav')

Test setup:
    HDD, NTFS

Windows 10 (1909), Python 3.7.0 64-bit:
    retrieve_files took 0.0277137s and scanned 2377 items, type: <class 'str'>
    retrieve_files_fnmatch took 0.0323329s and scanned 2378 items, type: <class 'str'>
    retrieve_files_glob took 0.03555950000000001s and scanned 2378 items, type: <class 'str'>
    retrieve_files_pathlib took 0.037946900000000006s and scanned 2378 items, type: <class 'pathlib.WindowsPath'>
* One file ends with ".WAV" in retrieve_files().

Xubuntu 20.04.1 LTS x86_64 (5.4.0-42-generic), Python 3.8.2 64-bit:
    retrieve_files took 0.040842309000026944s and scanned 2377 items, type: <class 'str'>
    retrieve_files_fnmatch took 0.03811149199998454s and scanned 2377 items, type: <class 'str'>
    retrieve_files_glob took 0.05661392199999682s and scanned 2377 items, type: <class 'str'>
    retrieve_files_pathlib took 0.06095831999999746s and scanned 2377 items, type: <class 'pathlib.PosixPath'>

Conclusion:
    - os.walk(path) & file.endswith(.wav) was consistently faster on Windows
    - os.walk(path) & fnmatch.filter(files, '*.wav') was consistently faster on Linux, all results being slower than Windows.
    
See https://www.python.org/dev/peps/pep-0471/
"""

import pathlib, os, glob, fnmatch
from timeit import default_timer as timer
from replace_sounds import CSTRIKE_PATH


def retrieve_files_pathlib(path: str) -> list:
    return [file for file in pathlib.Path(path).rglob('*.wav')]

def retrieve_files_glob(path: str) -> list:
    return [file for file in glob.glob(CSTRIKE_PATH + '/**/*.wav', recursive=True)]

def retrieve_files(path: str) -> list:
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.wav'):
                entry = os.path.join(root, file)
                files_list.append(entry)
    return files_list

def retrieve_files_fnmatch(path: str) -> list:
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, '*.wav'):
            entry = os.path.join(root, file)
            files_list.append(entry)
    return files_list

def print_timed_result(func, arg):
    start = timer()
    result = func(arg)
    end = timer()
    print(f'{func.__name__} took {end-start}s and scanned {len(result)} items, type: {type(result[0])}')


print_timed_result(retrieve_files, CSTRIKE_PATH)
print_timed_result(retrieve_files_fnmatch, CSTRIKE_PATH)
print_timed_result(retrieve_files_glob, CSTRIKE_PATH)
print_timed_result(retrieve_files_pathlib, CSTRIKE_PATH)
