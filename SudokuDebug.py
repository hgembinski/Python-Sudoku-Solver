#Haiden Gembinski
#Error handling & Debug functionality for Python Sudoku solver

#check if valid number
def check_num(num):
    try:
        i = int(num)
        if 1 <= i <= 9:
            return True
        else:
            return False
    except ValueError:
        return False

#check if it's a valid puzzle ie no duplicate numbers
def check_puzzle(puzzle):

    return False


#debug function to print puzzle to console
def print_puzzle(puzzle):
    print()
    for row in range(0,9):
        for column in range (0,9):
            print(puzzle[(row, column)], end = " ")
        print("")