import os
import shutil
import math
from PIL import Image


class Windows(object):
    root_dir = 'output/windows'
    Scale = {
        'factors': [1, 1.25, 1.5, 2, 4],
        'Sizes': [71, 150, 310, (310, 150), 44],
        'names': ['Square71x71Logo', 'Square150x150Logo', 'Square310x310Logo', 'Square310x150Logo', 'Square44x44Logo']
    }
    Targets = [16, 24, 32, 48, 256, 20, 30, 36, 40, 60, 64, 72, 80, 96]
    def __init__(self):
        super().__init__()

    def create_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            shutil.rmtree(directory)

    def resize_image(self, file, size_value, directory, output):
        with open(file, 'r+b') as f:
            with Image.open(f) as image:
                image.resize(size_value, Image.ANTIALIAS).save(
                    '{}/{}.{}'.format(directory, output, file.split('.')[-1]))

    def resize_scale(self, fileName):
        key = 'scale'
        work = Windows.Scale;
        for ind, value in  enumerate(work['Sizes']):
            sub_dir = "{}/{}/{}".format(Windows.root_dir, key, work['names'][ind])
            self.create_dir(sub_dir)
            for fac in work['factors']:
                name = "{}.{}-{}".format(fileName.split('.')[0], key, int(100*fac))
                size = value if isinstance(value, tuple) else (value, value)
                size = (math.ceil(size[0] * fac),  math.ceil(size[1] * fac))
                self.resize_image(fileName,size, sub_dir, name)

    def resize_target(self, fileName):
        key = 'targetsize'
        sub_dir = "{}/targetsize".format(Windows.root_dir)
        self.create_dir(sub_dir)
        for value in  Windows.Targets:
            name = "{}.targetsize-{}".format(fileName.split('.')[0], value)
            self.resize_image(fileName,(value, value), sub_dir, name)
    
    def resize(self, fileName):
        self.create_dir(Windows.root_dir)
        self.resize_scale(fileName)
        self.resize_target(fileName)
