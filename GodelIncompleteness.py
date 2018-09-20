import tkinter as tk
from tkinter import *

welcomeWindow = None


def GUIMain():
    '''Our GUI function. This function is called when the program is run. It creates a welcome window with a label, image, and import button.'''

    global welcomeWindow

    #this creates our welcome window
    welcomeWindow = tk.Tk()
    welcomeWindow["bg"] = "white"
    welcomeWindow.title("Gödel Incompleteness Theorem")


    #design labels for the window
    welcomeLabel = Label(welcomeWindow)
    welcomeLabel["text"] = "Gödel Incompleteness Theorem" + "\n" + "Advanced Symbolic Logic"
    welcomeLabel["font"] = "Arial 24"
    welcomeLabel["bg"] = "white"
    welcomeLabel.grid(row=0, column=1,padx=(50,50),pady=(100,25))

    #design labels for the window
    welcomeLabel = Label(welcomeWindow)
    welcomeLabel["text"] = "Created by Kevin Shin on 9/19/18"
    welcomeLabel["font"] = "Arial 14"
    welcomeLabel["bg"] = "white"
    welcomeLabel.grid(row=2, column=1,padx=(50,50),pady=(15,5))

    #the import button
    startButton = Button(welcomeWindow)
    startButton["text"] = "Start"
    startButton["font"] = "Arial 12"
    startButton["bg"] = "#997711"
    startButton["fg"] = "blue"
    startButton["command"] = introWindow
    startButton.grid(row=3, column=1,padx=10,pady=(5,19))

    welcomeWindow.mainloop()


def introWindow():
    '''write some intro text here
    maybe contains buttons which go to different tools'''

    introWindow = tk.Tk()
    introWindow.title("Axioms and Language")


    welcomeWindow.destroy()
    introWindow.mainloop()


def axiomWindow():
    '''displays axioms, does nothing fancy - need latex stuff in here'''

    global axiomWindow
    global welcomeWindow

    #allows the user to pick a file, then turns the photo into a tkImage, one which we need to actually display the photo in tkinter


    #main window and canvas
    axiomWindow = tk.Tk()
    axiomWindow.title("Axioms and Language")


    welcomeWindow.destroy()
    axiomWindow.mainloop()

GUIMain()