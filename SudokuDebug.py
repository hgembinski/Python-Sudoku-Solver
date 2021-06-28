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
def check_puzzle(puzzle, entries):
    nums = []

    #check the rows
    for i in range(0, 9):
        for j in range(0,9):
            if puzzle[i,j] in nums: #if this number already exists in the row, return false
                entries[i,j].config(background = "indianred3", disabledbackground = "indianred3")
                return False
            elif puzzle[i,j] != 0: #else add it to the check array, ignoring any 0's
                nums.append(puzzle[i,j])
        nums.clear()

    #check the column
    nums.clear()
    for i in range(0, 9):
        for j in range(0,9):
            if puzzle[j,i] in nums: #if this number already exists in the column, return false
                entries[i,j].config(background = "indianred3", disabledbackground = "indianred3")
                return False
            elif puzzle[j,i] != 0: #else add it to the check array, ignoring any 0's
                nums.append(puzzle[j,i])
        nums.clear()

    #check the sudoku "box"

    return True


#debug function to print puzzle to console
def print_puzzle(puzzle):
    print()
    for row in range(0,9):
        for column in range (0,9):
            print(puzzle[(row, column)], end = " ")
        print("")