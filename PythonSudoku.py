#Haiden Gembinski
#Python Sudoku Solver using tkinter
#Main file

import SudokuGUI
from SudokuGUI import *

#Main game screen
def play_sudoku():
    root = tkinter.Tk()
    root.title("Sudoku Solver")
    root.geometry("433x575")
    root.configure(background = 'light blue')
    title = Label(root,text = "PYTHON SUDOKU SOLVER", bg = 'light blue', 
            font = (None, 20)).grid(row = 0, column = 0, columnspan = 10)
    instructions = Label(root, text = "Input your numbers and then click Go!", bg = 'light blue', 
            font = (None, 15)).grid(row = 1,column = 0, columnspan = 10)

    frames = {}
    entries = {}

    for row in range(2, 11):
        for column in range(1, 10):

            #differentiate sudoku "squares" in UI
            if ((row in (2, 3, 4, 8, 9, 10) and column in (4, 5, 6)) or (row in (5, 6, 7) and column in (1, 2, 3, 7, 8, 9))):
                color = 'black'

            else:
                color = 'light blue'
            
            #create frames for sudoku board
            cell = Frame(root, highlightbackground = color,
                         highlightcolor = color, highlightthickness = 2,
                         width = 50, height = 50,  padx = 5,  pady = 5, background = 'black')
            cell.grid(row=row, column=column)
            frames[(row, column)] = cell

            #place entry objects in frame cells
            e = Entry(frames[row, column],font = (None, 20), justify = CENTER, width = 2)
            entries[(row - 2, column - 1)] = e
            e.pack()
    
    #place buttons
    go_button = Button(root, width = 5, bg = 'green', activebackground = 'light green', text = "Go!", 
                        font = (None, 20), command = lambda : solve_button(entries, root)).grid(row = 12, column = 0, columnspan = 5)

    clear_button = Button(root, width = 5, bg = 'red', activebackground = 'pink', text = "Clear", 
                        font = (None, 20), command = lambda : clear_UI_button(entries)).grid(row = 12, column = 6, columnspan = 5)

    root.mainloop()

play_sudoku()
