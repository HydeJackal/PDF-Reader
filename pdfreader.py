from tkinter import *
import reader
import speaker

class App:

  def __init__(self,master):
    frame=Frame(master)
    frame.pack()

    self.label=Label(frame, text="Welcome to the PDF reader.")
    self.label.pack()

    self.button = Button(frame, text="Quit", command=frame.quit)
    self.button.pack(side=LEFT)

    self.hi_there = Button(frame, text="Hello", command=self.say_hi())
    self.hi_there.pack(side=RIGHT)

  def say_hi(self):
      print("hi there, everyone!")

window = Tk()
app=App(window)

window.mainloop()
window.destory()