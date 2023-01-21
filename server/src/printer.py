import os


def image(data):

    # Get the data from the form
    data = data.files['file']
    data.save("image.png")
    os.system("feh image.png")

    return "OK"

