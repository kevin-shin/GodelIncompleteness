import tkinter as tk
import webbrowser
from tkinter import *
from PIL import ImageTk, Image

from src.mathHelperFunctions import *
from src.parser import *

url = "https://plato.stanford.edu/entries/goedel-incompleteness/"

symbolDict = {'0':1,'s':2,'+':3,'*':4,'=':5,'(':6,')':7,'|':8,'x':9,',':10,'~':11,'&':12,'∃':13}
numDict = {1:'0',2:'s',3:'+',4:'*',5:'=',6:'(',7:')',8:'|',9:'x',10:',',11:'~',12:'&',13:'∃'}

'''Differs from Crossley symbols because user needs to be able to type in'''

def GUIMain():
    '''This function is called when the program is run.'''

    global welcomeWindow
    welcomeWindow = tk.Tk()
    welcomeWindow["bg"] = "white"
    welcomeWindow.title("Gödel Incompleteness Theorem")

    welcomeLabel = Label(welcomeWindow)
    welcomeLabel["text"] = "Gödel Incompleteness Theorem" + "\n" + "Advanced Symbolic Logic"
    welcomeLabel["font"] = "Arial 24"
    welcomeLabel["bg"] = "white"
    welcomeLabel.grid(row=0, column=1,padx=(50,50),pady=(100,15))

    welcomeLabel = Label(welcomeWindow)
    welcomeLabel["text"] = "Created by Kevin Shin, 2018-2019"
    welcomeLabel["font"] = "Arial 14"
    welcomeLabel["bg"] = "white"
    welcomeLabel.grid(row=2, column=1,padx=(50,50),pady=(0,50))

    startButton = Button(welcomeWindow)
    startButton["text"] = "Start"
    startButton["font"] = "Arial 12"
    startButton["bg"] = "#997711"
    startButton["fg"] = "blue"
    startButton["command"] = introWindow
    startButton.grid(row=3, column=1,padx=(10,50),pady=(5,50))

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
    numberingButton["command"] = numberWindow
    numberingButton.grid(row=2, column=1,padx = 15)

    encodeButton = Button(Frame1)
    encodeButton["text"] = "Encode"
    encodeButton["font"] = "Arial 12"
    encodeButton["bg"] = "#997711"
    encodeButton["fg"] = "blue"
    encodeButton["command"] = encodeWindow
    encodeButton.grid(row=3, column=1)

    decodeButton = Button(Frame1)
    decodeButton["text"] = "Decode"
    decodeButton["font"] = "Arial 12"
    decodeButton["bg"] = "#997711"
    decodeButton["fg"] = "blue"
    decodeButton["command"] = decodeWindow
    decodeButton.grid(row=4, column=1)

    proofButton = Button(Frame1)
    proofButton["text"] = "Proof"
    proofButton["font"] = "Arial 12"
    proofButton["bg"] = "#997711"
    proofButton["fg"] = "blue"
    proofButton["command"] = showProof
    proofButton.grid(row=5, column=1,pady=(0,40))

    welcomeWindow.destroy()
    introWindow.mainloop()


def axiomWindow():
    '''displays axioms, does nothing fancy - need latex stuff in here'''

    global axiomWindow
    global welcomeWindow

    axiomWindow = tk.Tk()
    axiomWindow.geometry("800x850")
    axiomWindow.title("Axioms")

    axiomImage = ImageTk.PhotoImage(Image.open('../images/Axioms.jpg'))

    axiomCanvas = Canvas(axiomWindow)
    axiomCanvas.pack(expand=YES, fill=BOTH)
    axiomCanvas.create_image(50, 10, image=axiomImage, anchor=NW)

    axiomWindow.mainloop()


def numberWindow():
    global numberingWindow

    numberingWindow = tk.Tk()
    numberingWindow.geometry("375x550")
    numberingWindow.title("Godel Numbering System by Crossley")

    godelImage = ImageTk.PhotoImage(Image.open('../images/GodelKey.jpg'))
    numberingCanvas = Canvas(numberingWindow)
    numberingCanvas.pack(expand=YES, fill=BOTH)
    numberingCanvas.create_image(50, 5, image=godelImage, anchor=NW)

    numberingWindow.mainloop()


def encodeWindow():

    '''takes in a string, converts into Godel's Number'''

    global formulaLabel
    global formulaEntry
    global languageText
    global messageText

    encodeWindow = tk.Tk()
    encodeWindow.geometry("700x500")
    encodeWindow.title("Encoding Formulas by Godel Numbering")

    saveLabel = Label(encodeWindow, anchor="w")
    saveLabel["text"] = "Enter a formula:"
    saveLabel["font"] = "Arial 14"
    saveLabel["bg"] = "white"
    saveLabel.grid(row=0, column=0,pady=(15,5))

    formulaEntry = Entry(encodeWindow, bg = 'white', bd = 0.5, font = "Arial 14",
                justify= CENTER, width = 75)
    formulaEntry.grid(row=2,column=0,padx=10,pady=(0,15))
    formulaEntry.bind("<Return>",convertFormula)

    textLabel = Label(encodeWindow)
    textLabel["anchor"] = 'w'
    textLabel.pack(fill=BOTH, expand=True)
    textLabel.grid(row=4, column=0, padx=0, pady=5)
    messageText = StringVar()
    textLabel["textvariable"] = messageText

    formulaLabel = Label(encodeWindow)
    formulaLabel["anchor"] = 'w'
    formulaLabel.pack(fill=BOTH, expand=True)
    formulaLabel.grid(row=3, column=0, padx=0, pady=5)
    languageText = StringVar()
    formulaLabel["textvariable"] = languageText

def decodeWindow():

    '''takes in number, outputs string'''

    global formulaLabel
    global numberEntry
    global numberCanvas

    decodeWindow = tk.Tk()
    decodeWindow.title("Decoding a Godel Number to Formula")

    saveLabel = Label(decodeWindow, anchor="w")
    saveLabel["text"] = "Enter a number:"
    saveLabel["font"] = "Arial 14"
    saveLabel["bg"] = "white"
    saveLabel.grid(row=0, column=1,pady=(15,5))

    numberEntry = Entry(decodeWindow, bg = 'white', bd = 0.5, font = "Arial 14",
                justify = CENTER, width=40)
    numberEntry.grid(row=2,column=1,padx=10,pady=(0,15))
    numberEntry.bind("<Return>",decodeOutput)

    numberCanvas = Canvas(decodeWindow)
    numberCanvas.pack(expand=TRUE, fill='both')
    numberCanvas.grid(row=3, column=1, padx=30, pady=5)

def numberToText(number):
    primes = dictToList(primeFactorization(number))
    text =''
    for prime in primes:
        text = text + numDict[prime[1]]
    return text

def decodeOutput(event):
    userNumber = int(numberEntry.get())
    formula = numberToText(userNumber)
    formula = formula + ";"
    yacc.parse(formula)
    if event.keysym == "Return":
        numberCanvas.delete("all")
        formula = formula[:-1]
        numberCanvas.create_text(150, 10, text=formula, justify=tk.LEFT)
        if not yacc.parsedCorrectly:
            numberCanvas.create_text(150, 50, text="Not well formed.")
            yacc.parsedCorrectly = True

def convertFormula(event):
    global saveText
    global returnedNumber

    if event.keysym == "Return":
        languageText.set("")

    userText = formulaEntry.get()
    userText += ";"
    yacc.parse(userText)
    if not yacc.parsedCorrectly:
            messageText.set("Parsed Incorrectly. Not well formed.")
            yacc.parsedCorrectly = True
    else:
        userText = userText[:-1]
        if userText == '0':
            languageText.set("Converted Into Language: 1" + "\n" +
                             "Encoded into primes: 2^1" + "\n" +
                             "Godel Number: 2")
        else:
            i = 0
            j = 0

            returnedNumber = 1
            returnedString = ''
            returnedPrimes = ''

            for char in userText:
                if char not in symbolDict.keys():
                    languageText.set("")
                    messageText.set("Please use the Godel Numbering specified.")
                else:
                    returnedString = returnedString + str(symbolDict[char])
            lenFormula = len(returnedString)
            primesToUse = generatePrimes(lenFormula)

            for char in returnedString:
                returnedPrimes = returnedPrimes + str(primesToUse[i]) + '^' + char + "*"
                i += 1

            for char in returnedString:
                returnedNumber *= primesToUse[j]**int(char)
                j += 1

            returnedPrimes = returnedPrimes[:-1]
            messageText.set("")
            languageText.set("Converted Into Language: " +returnedString + "\n" +
                             "Encoded into primes: " + returnedPrimes + "\n" +
                             "Godel Number: " + str(returnedNumber))

def showProof():
    webbrowser.open_new(url)



GUIMain()
