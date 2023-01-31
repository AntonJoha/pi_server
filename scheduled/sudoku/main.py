import os
from escpos.printer import Network
from PIL import Image
from make_image import make_image
from generate import get_puzzle


puzzle = get_puzzle()
make_image(puzzle, "sudoku.png")

os.system("convert sudoku.png -resize 570x100000 sudoku.png")

printer = Network("192.168.0.157") #Printer IP Addreskks
printer.image("sudoku.png")
printer.cut()




