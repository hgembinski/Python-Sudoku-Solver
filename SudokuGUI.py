#Haiden Gembinski
#GUI functionality for Python Sudoku Solver

from SudokuMath import solve_sudoku
import tkinter
from tkinter import *
import SudokuDebug
from SudokuDebug import *

#function to build the main sudoku UI screen
def build_ui():
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

#CLEAR button functionality -> clears the sudoku board
def clear_UI_button(entries):
    enable_board(entries)
    for row in range(0,9):
        for column in range (0,9):
            entries[row,column].config(background = "white")
            entries[row,column].delete(0, END)

#GO button functionality -> solves the sudoku puzzle
def solve_button(entries, root):
    puzzle = {}

    #gets any inputted numbers from the UI and inserts them into the puzzle tuple (any blanks are replaced with 0)
    for row in range(0,9):
        for column in range (0,9):
            if entries[row,column].get() == "":
                puzzle[(row, column)] = 0
            else:
                if (check_num(entries[row,column].get())): #input validation
                    puzzle[(row, column)] = int(entries[row,column].get()) #insert each number as int in puzzle tuple
                    entries[row,column].config(background = "white", disabledbackground = "light green") #sets the bg color to green if it's an inputted number
                    entries[row,column].config(state='disabled')
                else:
                    entries[row,column].config(background = "indianred3") #sets the bg color to red if it's an errored number
                    enable_board(entries)
                    invalid_input_screen(root)
                    return

    solve_sudoku(puzzle, root, entries)

#re-enables the board and resets bg color of entry objects
def enable_board(entries):
    for row in range(0,9):
        for column in range (0,9):
            entries[row,column].config(state='normal')
            entries[row,column].config(background = "white", disabledbackground = "white") #resets bg color

#Error screen for invalid puzzle input
def invalid_input_screen(root):
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
                    command = lambda : error_close_button(error_screen)).pack(side = TOP)

#error screen if puzzle is invalid
def invalid_puzzle_screen(root):
    error_screen = tkinter.Toplevel(root)
    error_screen.title("Error!")

    x = root.winfo_x()
    y = root.winfo_y()
    h = root.winfo_height()
    w= root.winfo_width()
    error_screen.geometry("%dx%d+%d+%d" % (w - 100, h - 200, x + 50,y +50))
    error_screen.configure(background = "light blue")

    error_label_1 = Label(error_screen, text = "Invalid Puzzle", font = (None, 30), bg = "light blue", pady = 25).pack(fill = BOTH, side = TOP)
    error_label_2 = Label(error_screen, text = "Did you accidentally input a duplicate number?", 
                    font = (None, 20), bg = "light blue", pady = 50).pack(fill = BOTH, side = TOP)
    close_button = Button(error_screen, width = 5, text = "Close", font = (None, 30), bg = "royal blue", 
                    command = lambda : error_close_button(error_screen)).pack(side = TOP)

#CLOSE button for error screen functionality -> closes error screen and re-enables board
def error_close_button(error_screen):
    error_screen.destroy()


    mainloop()