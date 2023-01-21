import os
import queue
from flask import Flask
from flask import request
import threading
import time

from raspcheck import on_pi
import try_inky
from printer import image

app = Flask(__name__)
order = queue.Queue()
keep_going = True

def handle_queue():
    while keep_going:
        try:
            item = order.get(block=True, timeout=60)
            try_inky.set_screen(item)
            if on_pi():
                time.sleep(60)
        except queue.Empty:
            print("Empty")

def add_image(data):
    if order.qsize() > 15:
        return "List is full"
    order.put(data, block=True, timeout=None)
    return "Order added"




@app.get("/")
def handle_info():
    """
    This is what's seen if someone just opens the port in the web browser 
    """
    
    data = ""
    with open('form.html', 'r') as file:
        data = file.read().replace('\n', '')

    return data


@app.get("/image")
def get_image():
    """
    This is what's seen if someone just opens the port in the web browser 
    """
    
    data = ""
    with open('image.html', 'r') as file:
        data = file.read().replace('\n', '')

    return data



@app.post("/image")
def post_image():
    image(request)

    data = ""
    with open('image.html', 'r') as file:
        data = file.read().replace('\n', '')

    return data




@app.post("/info")
def handle():
    """
    This is what's seen if someone posts data to the port
    """
    
    # Get the data from the form
    data = request.form['say']
    print(data)
    
    
    return "OK"

@app.post("/")
def handle_start():
    """
    This function is called everytime your snake is entered into a game.
    request.json contains information about the game that's about to be played.
    """
    data = request.get_json()
    return add_image(data)


if __name__ == "__main__":
    print("Starting server...")
    th = threading.Thread(target=handle_queue)
    th.start()

    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port, debug=True)
    keep_going = False
    th.join()
