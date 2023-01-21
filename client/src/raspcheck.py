import os

pi = None

def on_pi():
    global defined
    global pi
    if pi is None:
        pi = _on_pi()
    return pi

def _on_pi():
    return os.system('raspinfo > /dev/null 2>&1') == 0
