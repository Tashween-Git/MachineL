from tkinter import *
from tkinter import ttk
import text_review


def foo():
    review = entry.get()
    if review:
        rating = text_review.get_rating(review)

        for x in rating:
            rating=x
        overall_score.set(str(x))
    else:
        print("Please enter some text")


root = Tk()

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2


print(x)
print(y)


root.geometry("640x300+" +str(int(x)) +"+" + str(int(y)))

root.title("Overall Rating")
#root.geometry("640x450+0+0")

heading = Label(root, text="Text Review Prediction", font=("arial", 20, "bold"), fg="steelblue").pack()

text_entry_label = Label(root, text="Input text: ")
text_entry_label.place(x=200,y=50)

entry = Entry(root)
entry.place(x=300, y=50)

overall_score = StringVar()
overall_score_label = Label(root, textvariable=overall_score, font=("arial", 20))
overall_score_label.place(x=300, y=150)

get_value = Button(text="Get Rating", command=foo)
get_value.place(x=300, y=250)


root.mainloop()