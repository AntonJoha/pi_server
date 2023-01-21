from inky.mock import InkyMockImpression
from inky import Inky7Colour
from raspcheck import on_pi


inky = None


def new_inky():
    global inky
    if on_pi():
        inky = Inky7Colour()
    else:
        inky = InkyMockImpression()


def get_inky():
    if inky is None:
        new_inky()
    return inky
