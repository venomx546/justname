import tkinter
import random
from tkinter import ttk
import time
from tkinter import *


window = tkinter.Tk()
window.title("Russian Roulette")

photo = PhotoImage(file = "D:\pycharm\photo\RR.png")
label = Label(image = photo)
label.grid (row = 0, column = 1)

labelOne = ttk.Label(window, text = "To spin the gun type spin: ")
labelOne.grid(row = 5, column = 0)

labelTwo = ttk.Label(window, text= "")
labelTwo.grid(row = 6, column = 1)

labelThree = ttk.Label(window, text= "")
labelThree.grid(row = 7, column = 1)

labelFour = ttk.Label(window, text= "")
labelFour.grid(row = 8, column = 1)

labelFive = ttk.Label(window, text= "")
labelFive.grid(row = 9, column = 1)

labelSix = ttk.Label(window, text= "")
labelSix.grid(row = 10, column = 1)

labelSeven = ttk.Label(window, text= "")
labelSeven.grid(row = 11, column = 1)

labelEight = ttk.Label(window, text= "")
labelEight.grid(row = 12, column = 1)

labelNine = ttk.Label(window, text= "")
labelNine.grid(row = 13, column = 1)

Spin = tkinter.StringVar()

spinentry = ttk.Entry(window, width = 88, textvariable = Spin)
spinentry.grid(row = 5, column = 1)

def thespin():
    while Spin.get() == "spin":
        labelTwo.configure(text = "Loading Bullets...")
        time.sleep(1)
        labelThree.configure(text = "Spinning...")
        time.sleep(2)
        b = random.randrange(1, 7)
        c = list()
        c.append(b)
        labelFour.configure(text = c)

        if b == 3 or b == 5:
            labelFive.configure(text = "*Takes The Gun*")
            time.sleep(1)
            labelSix.configure(text = "*Gun Shoots*" )
            time.sleep(1)
            labelSeven.configure(text = "Bullet")
            labelEight.configure(text = "RIP!")
            labelNine.configure(text="To Start Over Press the Button!")


        elif b != 3 or b !=5:
            labelFive.configure(text="*Takes The Gun*")
            time.sleep(1)
            labelSix.configure(text="*Gun shoots*")
            time.sleep(1)
            labelSeven.configure(text="No Bullet")
            labelEight.configure(text="You Survived!")
            labelNine.configure(text="To Continue Press the Button!")

        break


btn = ttk.Button(window, text = "...", command = thespin)
btn.grid(row = 5, column = 2)

window.mainloop()