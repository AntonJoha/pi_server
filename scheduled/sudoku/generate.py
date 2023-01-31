import random
import copy
from Solve import solve
random.seed()

def check_square(puzzle, row, col):
    """Check if the square is valid"""
    l = []
    for i in range(3):
        for j in range(3):
            if puzzle[i + row * 3][j + col * 3] in l:
                return False
            if puzzle[i + row * 3][j + col * 3] != 0:
                l.append(puzzle[i + row * 3][j + col * 3])
    return True

def check_col(puzzle, col):
    """Check if the column is valid"""
    l = []
    for i in range(9):
        if puzzle[i][col] in l:
            return False
        if puzzle[i][col] != 0:
            l.append(puzzle[i][col])
    return True

def check_row(puzzle, row):
    """Check if the row is valid"""
    l = []
    for i in range(9):
        if puzzle[row][i] in l:
            return False
        if puzzle[row][i] != 0:
            l.append(puzzle[row][i])
    return True

def check(puzzle):
    """Check if the puzzle is valid"""
    for i in range(9):
        if not check_row(puzzle, i):
            return False
        if not check_col(puzzle, i):
            return False
    for i in range(3):
        for j in range(3):
            if not check_square(puzzle, i, j):
                return False
    return True

def get_empty_puzzle():
    """Generate an empty sudoku puzzle"""
    puzzle = []
    for i in range(9):
        puzzle.append([0] * 9)

    return puzzle

def brute_force(puzzle, i=0, j=0):
    """Brute force the puzzle"""
    if i >= 9:
        i = 0
        j += 1
        if j == 9:
            return True
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(l)

    if puzzle[i][j] != 0:
        return brute_force(puzzle, i + 1, j)
    for k in l:
        puzzle[i][j] = k
        if check(puzzle):
            next = brute_force(puzzle, i + 1, j)
            if next:
                return True
        puzzle[i][j] = 0
    return False

def add_random(puzzle):
    """Add random values to the board and solves it"""
    # Fill the board with 20 random numbers
    
    for i in range(5):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        value = random.randint(1, 9)
        puzzle[row][col] = value
        if check(puzzle) == False:
            puzzle[row][col] = 0


def remove_values(puzzle):
    """Remove values from the puzzle"""
    # Remove 40 values from the puzzle
    for i in range(100):
        old = 0
        row = 0
        col = 0
        while old == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            old = puzzle[row][col]
        puzzle[row][col] = 0
        c = copy.deepcopy(puzzle)
        if solve(c) == False:
            puzzle[row][col] = old


def print_puzzle(puzzle):
    """Print the puzzle"""
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end=" ")
        print()

def get_puzzle():
    """Generate a sudoku puzzle"""

    puzzle = get_empty_puzzle()
    #possible options
    
    add_random(puzzle)

    brute_force(puzzle)
    remove_values(puzzle)
    return puzzle


