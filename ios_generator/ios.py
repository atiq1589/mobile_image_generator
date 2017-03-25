import os
import shutil

from PIL import Image


class iOS(object):
    root_dir = 'output/apple'
    iPhone = {
        'iTunesArtwork': 512,
        'iTunesArtwork@2x': 1024,
        'Icon-60@2x': 120,
        'Icon-60@2x': 180,
        'Icon-76': 76,
        'Icon-76@2x': 152,
        'Icon-83.5@2x': 167,
        'Icon-Small-40': 40,
        'Icon-Small-40@2x': 80,
        'Icon-Small-40@3x': 120,
        'Icon-Small': 29,
        'Icon-Small@2x': 58,
        'Icon-Small@3x': 87
    }
    iPhone_legacy = {
        'Icon': 57,
        'Icon@2x': 114,
        'Icon-72': 72,
        'Icon-72@2x': 144,
        'Icon-Small': 29,
        'Icon-Small@2x': 58,
        'Icon-Small-50': 50,
        'Icon-Small-50@2x': 100,
    }
    iPad = {
        'iTunesArtwork': 512,
        'iTunesArtwork@2x': 1024,
        'Icon-76': 76,
        'Icon-76@2x': 152,
        'Icon-83.5@2x': 167,
        'Icon-Small-40': 40,
        'Icon-Small-40@2x': 80,
        'Icon-Small': 29,
        'Icon-Small@2x': 58
    }

    iPad_legacy = {
        'Icon-72': 72,
        'Icon-72@2x': 144,
        'Icon-Small-50': 50,
        'Icon-Small-50@2x': 100,
    }

    universal = {
        'iTunesArtwork': 512,
        'iTunesArtwork@2x': 1024,
        'Icon-60@2x': 120,
        'Icon-60@2x': 180,
        'Icon-76': 76,
        'Icon-76@2x': 152,
        'Icon-83.5@2x': 167,
        'Icon-Small-40': 40,
        'Icon-Small-40@2x': 80,
        'Icon-Small-40@3x': 120,
        'Icon-Small': 29,
        'Icon-Small@2x': 58,
        'Icon-Small@3x': 87
    }
    universal_legacy = {
        'Icon': 57,
        'Icon@2x': 114,
        'Icon-72': 72,
        'Icon-72@2x': 144,
        'Icon-Small': 29,
        'Icon-Small@2x': 58,
        'Icon-Small-50': 50,
        'Icon-Small-50@2x': 100,
    }
    iWatch = {
        'AppIcon40x40@2x': 80,
        'AppIcon44x44@2x': 88,
        'AppIcon86x86@2x': 172,
        'AppIcon98x98@2x': 196,
        'AppIcon24x24@2x': 48,
        'AppIcon27.5x27.5@2x': 55,
        'AppIcon29x29@2x': 58,
        'AppIcon29x29@3x': 87
    }
    iMessage = {
        'Messages1024x768': (1024, 768),
        'Messages60x45@2x': (120, 90),
        'Messages60x45@3x': (180, 135),
        'Messages67x50@2x': (134, 100),
        'Messages74x55@2x': (148, 110),
        'Messages27x20@2x': (54, 40),
        'Messages27x20@3x': (81, 60),
        'Messages32x24@2x': (64, 48),
        'Messages32x24@3x': (96, 72),
    }

    custom_icons = {
        '{}': 32,
        '{}@2x': 64,
        '{}@3x': 96
    }

    def __init__(self):
        super().__init__()
        self.works = [{'iPhone': iOS.iPhone},
                      {'iPhone_legacy': iOS.iPhone_legacy},
                      {'iPad': iOS.iPad},
                      {'iPad_legacy': iOS.iPad_legacy},
                      {'universal': iOS.universal},
                      {'universal_legacy': iOS.universal_legacy},
                      {'iWatch': iOS.iWatch},
                      {'iMessage': iOS.iMessage},
                      {'custom_icons': iOS.custom_icons}]
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

    def resize(self, fileName):
        self.create_dir(iOS.root_dir)
        for work in self.works:
            key = list(work.keys())[0]
            sub_dir = "{}/app_icons/{}/".format(iOS.root_dir, key)
            self.create_dir(sub_dir)
            for key, value in work[key].items():
                name = key.format(fileName.split('.')[0]) if '{}' in key else key 
                self.resize_image(fileName, value if isinstance(
                    value, tuple) else (value, value), sub_dir, name)
