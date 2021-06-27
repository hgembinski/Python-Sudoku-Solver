#Haiden Gembinski
#Main file for Python Sudoku solver
import tkinter
from tkinter import *

def main():
    build_ui()

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
                color = 'white'
            
            #create grid cells
            cell = Frame(root, highlightbackground = color,
                         highlightcolor = color, highlightthickness = 2,
                         width = 50, height = 50,  padx = 5,  pady = 5, background = 'black')
            cell.grid(row=row, column=column)
            frames[(row, column)] = cell

            #place entry objects in grid cells
            e = Entry(frames[row, column],font = (None, 20), justify = CENTER, width = 2)
            entries[(row - 2, column - 1)] = e
            e.pack()
    
    #place buttons
    go_button = Button(root, width = 5, bg = 'green', activebackground = 'light green', text = "Go!", 
                        font = (None, 20)).grid(row = 12, column = 0, columnspan = 5)

    clear_button = Button(root, width = 5, bg = 'red', activebackground = 'pink', text = "Clear", 
                        font = (None, 20), command = lambda : clear_UI(entries))
    clear_button.grid(row = 12, column = 6, columnspan = 5)

    root.mainloop()

#clears the sudoku board
def clear_UI(entries):
    for row in range(0,9):
        for column in range (0,9):
            if entries[row,column].get() != "":
                entries[row,column].delete(0, END)
            



main()
