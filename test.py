import sys
from mobile_image_converter.android import Android
Android().resize(sys.argv[1])
Android().resize_splash(sys.argv[1])