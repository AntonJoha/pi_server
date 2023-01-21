from extract import set_texttv
import time
#from test import image_yo
from try_inky import set_screen
from raspcheck import on_pi
from weather import get_weather_image
from img import random_image

def _set_image(fun):
    set_screen(fun)
    if on_pi():
        time.sleep(60*2)
    else:
        time.sleep(10)


while True:
    _set_image(random_image)
    _set_image(get_weather_image)
    _set_image(set_texttv)
