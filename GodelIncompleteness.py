import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

welcomeWindow = None

symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,',':8,'x':9,'|':10,'~':11,'&':12,'∃':13}
'''differs from Crossley symbols because user needs to be able to type in'''



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

    introLabel = Label(introWindow)
    introLabel["bg"] = "white"
    introLabel.grid(row=0, column=0)
    introLabel["text"] = "SOME INTRO TEXT HERE ABOUT GODEL AND INCOMPLETENESS"



    Frame1 = Frame(introWindow)
    Frame1["bg"] = "white"
    Frame1.grid(row=1, column=2)

    # buttons corresponding to the functions
    axiomButton = Button(Frame1)
    axiomButton["text"] = "Axioms"
    axiomButton["font"] = "Arial 12"
    axiomButton["bg"] = "#997711"
    axiomButton["fg"] = "blue"
    axiomButton["command"] = axiomWindow
    axiomButton.grid(row=1, column=1)

    numberingButton = Button(Frame1)
    numberingButton["text"] = "Godel Numbering"
    numberingButton["font"] = "Arial 12"
    numberingButton["bg"] = "#997711"
    numberingButton["fg"] = "blue"
    #numberingButton["command"] = cloneClick
    numberingButton.grid(row=2, column=1)

    encodeButton = Button(Frame1)
    encodeButton["text"] = "Encode"
    encodeButton["font"] = "Arial 12"
    encodeButton["bg"] = "#997711"
    encodeButton["fg"] = "blue"
    encodeButton["command"] = encodeWindow
    encodeButton.grid(row=3, column=1)

    grayButton = Button(Frame1)
    grayButton["text"] = "Grayscale"
    grayButton["font"] = "Arial 12"
    grayButton["bg"] = "#997711"
    grayButton["fg"] = "blue"
    #grayButton["command"] = grayClick
    grayButton.grid(row=4, column=1)

    sepiaButton = Button(Frame1)
    sepiaButton["text"] = "Sepia"
    sepiaButton["font"] = "Arial 12"
    sepiaButton["bg"] = "#997711"
    sepiaButton["fg"] = "blue"
    #sepiaButton["command"] = sepiaClick
    sepiaButton.grid(row=5, column=1)


    welcomeWindow.destroy()
    introWindow.mainloop()



def axiomWindow():
    '''displays axioms, does nothing fancy - need latex stuff in here'''

    global axiomWindow
    global welcomeWindow

    axiomWindow = tk.Tk()
    axiomWindow.title("Axioms and Language")
    numberingWindow = tk.Tk()
    numberingWindow.title("Godel Numbering System by Crossley")

    axiomImage = ImageTk.PhotoImage(Image.open('EqualityAxioms.jpg'))
    peanoImage = ImageTk.PhotoImage(Image.open('PeanoAxioms.jpg'))
    inductionImage = ImageTk.PhotoImage(Image.open('Induction.jpg'))
    godelImage = ImageTk.PhotoImage(Image.open('GodelNumberingKey.jpg'))


    axiomCanvas = Canvas(axiomWindow)
    numberingCanvas = Canvas(numberingWindow)
    axiomCanvas.pack(expand=YES, fill=BOTH)
    axiomCanvas.create_image(50, 10, image=axiomImage, anchor=NW)
    axiomCanvas.create_image(50, 10, image=peanoImage, anchor=NW)
    axiomCanvas.create_image(50, 10, image=inductionImage, anchor=NW)
    numberingCanvas.create_image(50, 10, image=godelImage, anchor=NW)


    axiomWindow.mainloop()
    numberingWindow.mainloop()

def encodeWindow():

    '''takes in a string, converts into Godel's Number'''

    global formulaCanvas
    global formulaCanvas2
    global formulaEntry


    encodeWindow = tk.Tk()
    encodeWindow.title("Encoding Formulae by Godel Numbering")

    saveLabel = Label(encodeWindow, anchor="w")
    saveLabel["text"] = "Enter a formula:"
    saveLabel["font"] = "Arial 14"
    saveLabel["bg"] = "white"
    saveLabel.grid(row=0, column=1,pady=(15,5))

    formulaEntry = Entry(encodeWindow, bg = 'white', bd = 0.5, font = "Arial 14",
                justify = CENTER, width=40)
    formulaEntry.grid(row=2,column=1,padx=10,pady=(0,15))
    formulaEntry.bind("<Return>",convertFormula)

    formulaCanvas = Canvas(encodeWindow)
    formulaCanvas.grid(row=3, column=1, padx=30, pady=30)

    formulaCanvas2 = Canvas(encodeWindow)
    formulaCanvas2.grid(row=4, column=1, padx=30, pady=30)


def convertFormula(event):
    '''Takes in an event, in this case the pressing of the Return key by the user. When the Return key is pressed, this function will
    take the picture currently on the canvas and save this image under the name entered by the user in saveWindow.'''
    global saveText
    global returnedNumber

    if event.keysym == "Return": # examples of how to check what key
        formulaCanvas.delete("all")
        userText = formulaEntry.get()
        returnedNumber = ''
        for char in userText:
            if char not in symbolDict.keys():
                formulaCanvas.create
            else:
                returnedNumber = returnedNumber + str(symbolDict[char])
    formulaCanvas.create_text(100,10,text="Converted Into Language: "+returnedNumber, justify=tk.CENTER)




##---------MATH HELPER FUNCTIONS---------##

def isitprime(n):
    a = 2
    flag = True
    while a <= n/2:
        if n%a == 0:
            flag = False
            break
        else:
            a += 1
    return flag


def generatePrimes(number):
    start = number-2
    primes = [2,3]
    starter = 5
    while start != 0:
        if isitprime(starter):
            primes.append(starter)
            starter += 1
            start -= 1
        else:
            starter += 1
    return primes




GUIMain()