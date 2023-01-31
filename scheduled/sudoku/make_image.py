from generate import get_puzzle
from PIL import Image, ImageDraw, ImageFont


def draw_sudoku(puzzle, draw):
    """Draw the puzzle on the image."""
    # Draw the grid
    f = ImageFont.truetype("/nix/store/m8b8b23c360zlbcyz2ajs9jz47kf86jk-texlive-lato-3.3/fonts/truetype/typoland/lato/Lato-Semibold.ttf", 25)

    for i in range(10):
        # Draw a thick line every 3 squares
        if i % 3 == 0:
            width = 3
        else:
            width = 1
        # Draw the horizontal and vertical lines
        draw.line((0, i * 50, 450, i * 50), fill="black", width=width)
        draw.line((i * 50, 0, i * 50, 450), fill="black", width=width)
    # Draw the numbers
    for row in range(9):
        for col in range(9):
            # Get the number to draw
            number = puzzle[row][col]
            if number != 0:
                # Calculate the position of the number
                x = col * 50 + 25
                y = row * 50 + 25
                # Draw the number
                draw.text((x, y), str(number), fill="black", anchor="mm", font=f)

def make_image(puzzle, filename):
    """Make an image of the puzzle and save it to filename."""
    # Create a new image with a black background
    image = Image.new("RGB", (450, 450), "white")
    # Create a drawing object that is associated with the image
    draw = ImageDraw.Draw(image)
    # Draw the puzzle
    draw_sudoku(puzzle, draw)
    # Save the image to a file
    image.save(filename)

if __name__ == "__main__":
    # Make a puzzle
    puzzle = get_puzzle()
    # Make an image of the puzzle
    make_image(puzzle, "sudoku.png")
