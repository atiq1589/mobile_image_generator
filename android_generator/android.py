import os
import shutil

from PIL import Image
class Android(object):
    root_dir = 'android'
    subdir_prefix = 'drawable'
    icons = {
            'ldpi':36,
            'mdpi': 48,
            'hdpi': 72,
            'xhdpi': 96,
            'xxhdpi': 144,
            'xxxhdpi': 192,
            'play_store': 512,
         }
    splash = {
        'ldpi': (200, 320),
        'mdpi': (320, 480),
        'hdpi': (480, 800),
        'xhdpi': (720,1280),
        'xxhdpi': (960, 1600),
        'xxxhdpi': (1280, 1820),
    }
    def __init__(self):
        super().__init__()

    def resize_image(self, file, size_key, size_value, image_type='icons'): 
        with open(file, 'r+b') as f:
            with Image.open(f) as image:
                d = "{}/{}/{}_{}".format(Android.root_dir, image_type, Android.subdir_prefix, size_key)
                os.makedirs(d)
                image.resize(size_value, Image.ANTIALIAS).save('{}/{}'.format(d, file))

    def resize(self, fileName):
        if not os.path.exists(Android.root_dir):
            os.makedirs(Android.root_dir)
        else:
            shutil.rmtree(Android.root_dir)
        for key, value in Android.icons.items():
            self.resize_image(fileName, key, (value, value))

    def resize_splash(self, fileName):
        if not os.path.exists(Android.root_dir):
            os.makedirs(Android.root_dir)
        for key, value in Android.splash.items():
            self.resize_image(fileName, key, value, 'splash-protrait')
            self.resize_image(fileName, key, value[::-1], 'splash-landscape')