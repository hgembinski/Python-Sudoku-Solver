#Haiden Gembinski
#GUI functions for Python Sudoku Solver
import tkinter
from tkinter import *

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
                        font = (None, 20), command = lambda : solve_button(entries)).grid(row = 12, column = 0, columnspan = 5)

    clear_button = Button(root, width = 5, bg = 'red', activebackground = 'pink', text = "Clear", 
                        font = (None, 20), command = lambda : clear_UI_button(entries))
    clear_button.grid(row = 12, column = 6, columnspan = 5)

    root.mainloop()

#CLEAR button functionality -> clears the sudoku board
def clear_UI_button(entries):
    for row in range(0,9):
        for column in range (0,9):
            entries[row,column].config(state='normal')
            entries[row,column].config(disabledbackground = "white") #resets bg color
            if entries[row,column].get() != "":
                entries[row,column].delete(0, END)

#GO button functionality -> solves the sudoku puzzle
def solve_button(entries):
    puzzle = {}

    #gets any inputted numbers from the UI and inserts them into the puzzle tuple (any blanks are replaced with 0)
    for row in range(0,9):
        for column in range (0,9):
            if entries[row,column].get() == "":
                puzzle[(row, column)] = 0
                entries[row,column].insert(0, "0")
            else:
                puzzle[(row, column)] = entries[row,column].get()
                entries[row,column].config(disabledbackground = "light green") #sets the bg color to green if it's an inputted number
            entries[row,column].config(state='disabled')


#debug function to print puzzle to console
def print_puzzle(puzzle):
    for row in range(0,9):
        for column in range (0,9):
            print(puzzle[(row, column)], end = " ")
        print("")
        