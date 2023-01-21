import os
from escpos.printer import Network
from PIL import Image


def make_image(path):
    #get image dimensions
    width, height = Image.open(path).size
    #flip if width is greater than height
    if width > height:
        Image.open(path).rotate(90, expand=True).save(path)

    # Resize the image
    os.system("convert " + path + " -resize 570x100000 " + path)


def image(data):

    # Get the data from the form
    data = data.files['file']
    data.save("image.png")

    make_image("image.png")


    # Print the image
    printer = Network("192.168.0.157") #Printer IP Addreskks
    printer.image("image.png")
    printer.cut()

    return "OK"

