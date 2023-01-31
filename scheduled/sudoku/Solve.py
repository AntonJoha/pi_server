
def col_remove(puzzle, possible):
    """Remove values from the columns"""
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                for k in range(9):
                    if puzzle[i][j] in possible[k][j]:
                        possible[k][j].remove(puzzle[i][j])

def row_remove(puzzle, possible):
    """Remove values from the rows"""
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                for k in range(9):
                    if puzzle[i][j] in possible[i][k]:
                        possible[i][k].remove(puzzle[i][j])

def box_remove(puzzle, possible):
    """Remove values from the boxes"""
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                for k in range(3):
                    for l in range(3):
                        if puzzle[i][j] in possible[(i//3)*3+k][(j//3)*3+l]:
                            possible[(i//3)*3+k][(j//3)*3+l].remove(puzzle[i][j])

def get_possible():
    """A list of lists for use in the solving"""
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    to_return = []
    for _ in range(9):
        temp = list()
        for _ in range(9):
            temp.append(options.copy())
        to_return.append(temp)
    return to_return

def remove_single(puzzle, possible):
    """Solves all positions with a single possible value"""
    for i in range(9):
        for j in range(9):
            if len(possible[i][j]) == 1:
                puzzle[i][j] = possible[i][j][0]
                possible[i][j] = []


def single_row(puzzle, possible):
    """Find a variable which is the only one in its row with a certain value"""
    for i in range(9):
        for j in range(9):
            for opt in possible[i][j]:
                count = 0
                for k in range(9):
                    if opt in possible[i][k]:
                        count += 1
                if count == 1:
                    possible[i][j] = [opt]
                    break


def single_col(puzzle, possible):
    """Find a variable which is the only one in its row with a certain value"""
    for i in range(9):
        for j in range(9):
            for opt in possible[j][i]:
                count = 0
                for k in range(9):
                    if opt in possible[j][i]:
                        count += 1
                if count == 1:
                    possible[j][i] = [opt]
                    break




def count_solved(puzzle):
    count = 0
    for i in puzzle:
        for j in i:
            if j != 0:
                count += 1
    return count

def solve(puzzle):
    """Solves the sudoku based on human methods"""
    
    #Don't want to solve the actual puzzle

    possible_values = get_possible()
    
    # Remove all values that are already in the puzzle
    remove_single(puzzle, possible_values)

    count = count_solved(puzzle)

    while count != 81:
        col_remove(puzzle, possible_values)
        row_remove(puzzle, possible_values)
        box_remove(puzzle, possible_values)
        single_row(puzzle, possible_values)
        single_col(puzzle, possible_values)
        #single_box(puzzle, possible_values)

        remove_single(puzzle, possible_values)
        new = count_solved(puzzle)
        if new == count:
            return False
        count = new
    return True
        
