import hitherdither
from inky import auto
from PIL import Image
from get_inky import get_inky,new_inky
from raspcheck import on_pi
from io import BytesIO
import base64

def _dither_image(img):
    inky = get_inky()
    thresholds = [64, 64, 64]  # Threshold for snapping colours, I guess?
    palette = hitherdither.palette.Palette(inky._palette_blend(0.8, dtype='uint24'))
    new = hitherdither.ordered.bayer.bayer_dithering(img, palette, thresholds, order=8)
    return new.convert("P")


def _image_from_data(data):
    img = data['data'][1:]
    return Image.open(BytesIO(base64.urlsafe_b64decode(img)))

def set_screen(data):
    
    inky = get_inky()
    image = _image_from_data(data)
    image = image.resize(inky.resolution)

    if on_pi():
        image = _dither_image(image)
    
    inky.set_image(image)
    inky.show()
    
    #If it's a Mock
    if on_pi() == False:
        inky.wait_for_window_close()
        new_inky()
