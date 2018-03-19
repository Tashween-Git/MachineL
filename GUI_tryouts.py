from tkinter import *

def subscribe():
    print("Now Subscribing to me !!!")

root = Tk()
root.geometry("600x600")
button = Button(root, text="Print", command=subscribe)

button.pack()

root.mainloop()