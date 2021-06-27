#Haiden Gembinski
#Error handling & Debug functions for Python Sudoku solver

#debug function to print puzzle to console
def print_puzzle(puzzle):
    for row in range(0,9):
        for column in range (0,9):
            print(puzzle[(row, column)], end = " ")
        print("")