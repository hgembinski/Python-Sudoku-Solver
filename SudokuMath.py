#Haiden Gembinski
#Math functionality for Python Sudoku solver

#returns the solved puzzle
from SudokuDebug import *
from SudokuGUI import *


def solve_sudoku(unsolved_puzzle, root, entries):
    
    if check_puzzle(unsolved_puzzle, entries):
        solve(unsolved_puzzle)
    else:
        invalid_puzzle_screen(root) #show error screen if puzzle is invalid


#solves the sudoku puzzle
def solve(unsolved_puzzle):

    next_blank = find_blank(unsolved_puzzle)

    if not next_blank:
        return True
    
    else:
        row, column = next_blank

    for i in range(1,10):
        if valid_number(unsolved_puzzle, i, next_blank):
            unsolved_puzzle[row, column] = i

            if (solve(unsolved_puzzle)):
                return True

            unsolved_puzzle[row, column] = 0 #backtrack if i doesn't fit
    return False

#finds the next empty (represented as 0) space in the puzzle, returns None if one doesn't exist
def find_blank(puzzle):
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i, j] == 0:
                return (i, j) #returns the index of the blank

    return None

#returns true if a number fits in the given position on the board, false if not
def valid_number(puzzle, num, position):
    #get position of number
    row = position[0]
    column = position[1]

    #check the row
    for i in range(0,9):
        if puzzle[row, i] == num and column != i:
            return False
    
    #check the column
    for i in range(0,9):
        if puzzle[i, column] == num and row != i:
            return False

    #check the sudoku "box" that the number is in
    box_row = row // 3
    box_column = column // 3

    for i in range(box_row*3, (box_row*3)+3):
        for j in range(box_column*3, (box_column*3)+3):
            if puzzle[i, j] == num and row != i and column != j:
                return False
   
    return True #return true if everything checks out