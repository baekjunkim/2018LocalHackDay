from tkinter import *
from time import sleep
import random
import webbrowser

userId = "9176132006"
userPw = "132435"

canvasHeight = 1000
canvasWidth = 1000
canvasBorderBuffer = 10

global example

example = {"BAMA":[("t1","u1"),("t2","u2"),("t3","u3")],"Jalen":[("t1","u1"),("t2","u2"),("t3","u3")]}

ex = ""
for key in example.keys():
    ex += "\n"
    ex += key
    for value in example[key]:
        ex += "\n"
        ex += value[0]
        ex += "\n"
        ex += value[1]
        ex += "\n"


class createGUI():
    global rootWindow
    global canvas
    global statusLabel
    global idEntry
    global pwEntry
    global idLabel
    global pwLabel
    global buttonframe
    global loginStatus
    global button1
    global button2
    global button3
    global mainboard
    global link

    def login():
        idEntry.configure(state = 'disabled')
        pwEntry.configure(state = 'disabled')
        loginStatus.configure(text = 'logged in')
        canvas.create_text(100,200, text = ex)

    def callback(event):
        webbrowser.open_new(r"google.com")

    rootWindow = Tk()
    rootWindow.title("Twitter to google News")
    canvasAndButtons = Frame(rootWindow)
    canvas = Canvas(canvasAndButtons, height = canvasHeight, width = canvasWidth, relief = SUNKEN, borderwidth = 2)
    
    canvas.pack(side = LEFT)
    buttonframe = Frame(canvasAndButtons)
    

### log-in part
    idLabel = Label(buttonframe, text = "ID:", justify = CENTER)
    pwLabel = Label(buttonframe, text = "PW:", justify = CENTER)

    idEntry = Entry(buttonframe)
    pwEntry = Entry(buttonframe, show="*")
    loginButton = Button(buttonframe, text = "Sign in (Twitter)", fg = 'blue', command = login)
    loginStatus = Label(buttonframe, text = "Waiting for you")

        
    idLabel.pack()
    idEntry.pack()
    pwLabel.pack()
    pwEntry.pack()
    loginButton.pack()
    loginStatus.pack()

###
    link = Label (buttonframe, text = "go to google", fg = "blue", cursor = "hand2")
    link.pack()
    link.bind("<Button-1>", callback)

    buttonframe.pack(side=RIGHT)
    canvasAndButtons.pack()

def initTwitter():
    twitterId = idEntry.get()
    twitterPw = pwEntry.get()

