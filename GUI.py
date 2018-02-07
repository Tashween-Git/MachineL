from tkinter import *
import tkinter as tk


class CustomButton(tk.Canvas):
    def __init__(self, parent, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=1, relief="raised")
        self.command = command

        padding = 4

        self.loadimage = tk.PhotoImage(file="vh6fzb.png")
        self.roundedbutton = tk.Button(self, image=self.loadimage)
        #self.roundedbutton["bg"] = "white"
        self.roundedbutton["border"] = "0"

        self.roundedbutton.pack(side="top")

        def _on_press(self, event):
            self.configure(relief="sunken")

        def _on_release(self, event):
            self.configure(relief="raised")
            if self.command is not None:
                self.command()


root = Tk()

topFrame = Frame(root)
bottomFrame = Frame(root)

topFrame.pack()
bottomFrame.pack(side=BOTTOM)

x = "caca"
button1 = Button(bottomFrame, text="Calculate Accuracy", fg="red", bg="blue")
button2 = Button(bottomFrame, text=x, fg="black", bg="white")

label_ = Label(topFrame, text="Accuracy: ")

round = CustomButton(bottomFrame)

button4 = Button(bottomFrame, text="Click")
img = PhotoImage(file="vh6fzb.png")
button4.config(image=img)

button4.pack()
button1.pack()
button2.pack()
label_.pack()
round.pack()
root.mainloop()
