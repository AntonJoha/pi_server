import hitherdither
from inky import auto
from PIL import Image
from get_inky import get_inky,new_inky
from raspcheck import on_pi
import base64
from io import BytesIO
import requests

def _make_post(msg):
    url = "http://127.0.0.1:8080"
    obj = {'data': str(msg)}
    r = requests.post(url, json = obj)


def set_screen(fun):
    
    inky = get_inky()
    
    image = fun()
    
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.urlsafe_b64encode(buffered.getvalue())
    _make_post(img_str)

