import urllib.request
import io
import urllib.parse
import base64
import sys
import random

import hitherdither
from PIL import Image
from inky import auto
from get_inky import get_inky

def _get_image(page):
    url = "https://www.svt.se/text-tv/" + str(page)
    f = urllib.request.urlopen(url)
    site = f.read().decode('ISO-8859-1')


    pos = site.index("data:image/gif;base64,", 0 , len(site)) + 22
    newpos = site.index("\"", pos, len(site))

    to_decode = site[pos:newpos + 1]

    to_decode = site[pos:newpos + 1]
    fh = io.BytesIO()
    fh.write(base64.b64decode(to_decode))
    return fh

def _set_page(page):

    if (page < 100) or( page > 999):
        page = 100
    inky = get_inky()
    image = Image.open(_get_image(page)).convert("RGB")
    image_resized = image.resize(inky.resolution)
    return image_resized


def _get_possible_pages():
    toReturn = [*range(104, 200, 1)]
    toReturn.append(401)

    return toReturn

def set_texttv():
    list = _get_possible_pages()
    
    while True:
        try:
            print(random.choice(list))
            return _set_page(int(random.choice(list)))
        except:
            print("Error getting page retry")
