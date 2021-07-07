from PIL import Image
import os
from pathlib import Path



def multi_resize(img,*args):
    for i in args:
        Path(os.path.splitext(img)[0]).mkdir(parents=True, exist_ok=True)
        dir_path = './'+os.path.splitext(img)[0]+'/'
        image = Image.open(img)
        image = image.resize((i,i),Image.ANTIALIAS)
        image.save(os.path.join(dir_path,os.path.basename(str(i))),'JPEG')
        os.path.splitext(str(i)+'jpg')[0]
   
    return

def loop():
    try:
        folder_path=  './'
        icon_extension = '.jpg'
        img_list = []
        for img_file in os.listdir(folder_path):
            print(img_file)
            if img_file.endswith(icon_extension):

                print('Drawing image: {}'.format(folder_path + img_file))

                img_list.append(img_file)
                print(img_list)       
        return img_list
    except :
        print('loop fail')
for i in loop():
    multi_resize(i,1040,700,460,300,240)