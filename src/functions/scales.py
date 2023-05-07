from PIL.Image import BILINEAR, BICUBIC, LANCZOS, open as image_open
from os.path import getsize, exists
from os import listdir, mkdir
from functions.default_settings import *


class Scales:
    def __init__(self, folder=FOLDER, folder2=FOLDER2, threads=THREADS) -> None:
        self.folder = folder
        self.folder2 = folder2
        

    def downscale(self, new_dimensions=(600, 600), interpolation_level=3):
        self.dir_validation()
        
        for img in listdir(self.folder):
            img_path = f"{self.folder}/{img}"
            new_path = f"{self.folder2}/{img}"

            old_size = getsize(img_path)
            new_img = image_open(img_path)


            match interpolation_level:
                case 1: resized = new_img.resize(new_dimensions, resample=BILINEAR)

                case 2: resized = new_img.resize(new_dimensions, resample=BICUBIC)
                
                case 3: resized = new_img.resize(new_dimensions, resample=LANCZOS)
                
                case _: raise NameError("Invalid interpolation level")

            new_name = ""
            c = 1
            while exists(new_path):
                new_name = str(c)+img
                new_path = f"{self.folder2}/{new_name}"
                c+=1

            resized.save(new_path)
            new_size = getsize(new_path)

            print(f"[{old_size // 1000} kb] --> [{new_size // 1000} kb] {img}")


    def dir_validation(self):
        if not self.is_dir(self.folder): 
            mkdir(self.folder)
        if not self.is_dir(self.folder2): 
            mkdir(self.folder2)

    def is_dir(self, directory):
        if not exists(directory):
            return False
        return True
