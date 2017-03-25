import sys
from android_generator import Android
from ios_generator import iOS
from win_generator import Windows

Android().resize(sys.argv[1])
Android().resize_splash(sys.argv[1])

iOS().resize(sys.argv[1])


Windows().resize(sys.argv[1])