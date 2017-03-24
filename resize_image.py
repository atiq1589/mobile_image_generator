import sys
from PIL import Image

def resize_image(file, size): 
    with open(file, 'r+b') as f:
        with Image.open(f) as image:
            image.resize(size, Image.ANTIALIAS).save('{}-cover.jpeg'.format("".join( p for p in file.split('.')[0:-1]), image.format))

def main(*args):
    print (*args)
    resize_image(*args[0], (640, 560))

if __name__ == '__main__':
    main(sys.argv[1:])
