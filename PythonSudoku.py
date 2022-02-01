#Haiden Gembinski
#Python Sudoku Solver using tkinter
#Main file

import SudokuGUI
from SudokuGUI import *

#Main game screen
def play_sudoku():
    root = tkinter.Tk()
    gui = sudoku_gui(root)

    root.mainloop()

play_sudoku()