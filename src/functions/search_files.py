from os.path import exists
from os import remove, listdir
from win32api import SetFileAttributes
from functions.default_settings import *


def string_spliter():
    '''
    Separate strings from the TMP file into other TMP files according to the number of threads
    '''
    pass  

def create_thread_tmp_files():
    for t in range(THREADS):
        tmp_file = f"{TMP}{t}"

        if exists(tmp_file):
            remove(tmp_file)

        open(tmp_file, "x").close()
        SetFileAttributes(tmp_file, 0x02)

        THREAD_FILES.append(tmp_file)


def list_images():
    '''
    lists and saves the images in a temporary file
    '''
    if not is_dir(TMP):
        touch(TMP)
    else:
        remove(TMP)
        touch(TMP)

    with open(TMP, "a") as f:
        SetFileAttributes(TMP, 0x02) # attribute in hexadecimal that marks that a file is hidden is equivalent to 0x02 
        
        for img in listdir(FOLDER):
           f.write(f"{img}\n")


def touch(file):
    open(file, "x").close()


def is_dir(directory):
    if not exists(directory):
        return False
    return True
