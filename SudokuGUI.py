#Haiden Gembinski
#GUI functionality for Python Sudoku Solver

from SudokuMath import *
from SudokuChecks import *
import tkinter
from tkinter import *

#CLEAR button functionality -> clears the sudoku board
def clear_UI_button(entries):
    wipe_board(entries)
    for row in range(0,9):
        for column in range (0,9):
            entries[row,column].config(background = "white")
            entries[row,column].delete(0, END)

#GO button functionality -> solves the sudoku puzzle
def solve_button(entries, root):
    puzzle = {}

    #Gets any inputted numbers from the UI and inserts them into the puzzle tuple (any blanks are replaced with 0)
    for row in range(0,9):
        for column in range (0,9):
            if entries[row,column].get() == "":
                puzzle[(row, column)] = 0
            else:
                if (check_num(entries[row,column].get())): #input validation
                    puzzle[(row, column)] = int(entries[row,column].get()) #insert each number as int in puzzle tuple
                    entries[row,column].config(background = "light green", disabledbackground = "light green") #sets the bg color to green if it's an inputted number
                    entries[row,column].config(state='disabled')
                else:
                    entries[row,column].config(background = "indianred3", disabledbackground = "indianred3") #sets the bg color to red if it's an errored number
                    enable_board(entries)
                    invalid_input_screen(root, entries)
                    return

    if check_puzzle(puzzle, entries):
        solve_sudoku(puzzle, entries)
        disable_board(entries)

    else:
        invalid_puzzle_screen(root, entries) #show error screen if puzzle is invalid

#Re-enables the board and resets bg color of entry objects for a full wipe
def wipe_board(entries):
    for row in range(0,9):
        for column in range (0,9):
            entries[row,column].config(state='normal')
            entries[row,column].config(background = "white", disabledbackground = "white") #resets bg color

#Just re-enables the board without wiping
def enable_board(entries):
    for row in range(0,9):
        for column in range (0,9):
            entries[row,column].config(state='normal')

#Disables board
def disable_board(entries):
    for row in range(0,9):
        for column in range (0,9):
            entries[row,column].config(state='disabled')

#Error screen for invalid number input
def invalid_input_screen(root, entries):
    error_screen = tkinter.Toplevel(root)
    error_screen.title("Error!")

    x = root.winfo_x()
    y = root.winfo_y()
    h = root.winfo_height()
    w= root.winfo_width()
    error_screen.geometry("%dx%d+%d+%d" % (w - 100, h - 200, x + 50,y +50))
    error_screen.configure(background = "light blue")

    error_label_1 = Label(error_screen, text = "Invalid Input", font = (None, 30), bg = "light blue", pady = 25).pack(fill = BOTH, side = TOP)
    error_label_2 = Label(error_screen, text = "Please Try Again", font = (None, 30), bg = "light blue", pady = 50).pack(fill = BOTH, side = TOP)
    close_button = Button(error_screen, width = 5, text = "Close", font = (None, 30), bg = "royal blue", 
                    command = lambda : error_close_button(error_screen, entries)).pack(side = TOP)

#Error screen if puzzle is invalid
def invalid_puzzle_screen(root, entries):
    error_screen = tkinter.Toplevel(root)
    error_screen.title("Error!")

    x = root.winfo_x()
    y = root.winfo_y()
    h = root.winfo_height()
    w= root.winfo_width()
    error_screen.geometry("%dx%d+%d+%d" % (w - 100, h - 200, x + 50,y +50))
    error_screen.configure(background = "light blue")

    error_label_1 = Label(error_screen, text = "Invalid Puzzle", font = (None, 30), bg = "light blue", pady = 25).pack(fill = BOTH, side = TOP)
    error_label_2 = Message(error_screen, text = "Did you accidentally input a duplicate number?", 
                    font = (None, 20), bg = "light blue", justify = CENTER, pady = 30).pack(fill = BOTH, side = TOP)
    close_button = Button(error_screen, width = 5, text = "Close", font = (None, 30), bg = "royal blue", 
                    command = lambda : error_close_button(error_screen, entries)).pack(side = TOP)

#CLOSE button for error screen functionality -> closes error screen and re-enables board
def error_close_button(error_screen, entries):
    enable_board(entries)
    error_screen.destroy()
