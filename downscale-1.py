from PIL import Image
from os import path
import os

folder = "./imgs"
folder2 = "./imgs2"

if not path.exists(folder):
    os.mkdir(folder)
    print(folder + " created")

if not path.exists(folder2):
    os.mkdir(folder2)
    print(folder2 + " created")

interpolation_level = 3
new_dimensions = 600, 600

imgs = os.listdir(folder)

for _ in range(1):
    for img in imgs:
        img_path = folder+"/"+img
        new_path = folder2+"/"+img

        old_size = path.getsize(img_path)

        new_img = Image.open(img_path)

        if interpolation_level == 1:
            resized = new_img.resize(new_dimensions, resample=Image.BILINEAR)
        elif interpolation_level == 2:
            resized = new_img.resize(new_dimensions, resample=Image.BICUBIC)
        elif interpolation_level == 3:
            resized = new_img.resize(new_dimensions, resample=Image.LANCZOS)
        else:
            raise NameError("Invalid interpolation level")
        
        c = 1
        while path.exists(new_path):
            new_name = str(c)+img
            new_path = folder2+"/"+new_name
            c+=1

        resized.save(new_path)

        new_size = path.getsize(new_path)
        print(f"{img}: [{old_size // 1000} kb] --> {new_name}: [{new_size // 1000} kb]")

exit()