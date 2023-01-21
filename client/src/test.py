
from PIL import Image,  ImageEnhance, ImageFilter, ImageFont, ImageDraw
import easyrice

from get_inky import get_inky
from inky import auto

def image_yo():
    inp = None
    out = "out.png"
    conf = "gnu_free_config"
    com = "example_commands"

    easyrice.make_image(conf, com, out, inp)
    img = Image.open(out)

    inky = get_inky()
    image_resized = img.resize(inky.resolution)
    
    return image_resized
