from tkinter import *
import overall_rating as ov
import tkinter.messagebox
from tkinter import ttk

import glob
import os
import time

def get_filenames():
    csv = []
    csv = (glob.glob("E:\PycharmProjects\MachineL\Hotels Dataset\*.csv"))

    csvs =[]
    for x in csv:
        csvs.append((os.path.basename(x).replace(".csv", "")))

    return csvs

def stop():
    root.after(1000, pb.stop())

def display(score_array, pred):
    booking.set(score_array[0])
    expedia.set(score_array[1])
    agoda.set(score_array[2])
    google.set(score_array[3])
    my.set(pred)
    total = 0

    for x in score_array:
        total += float(x)

    total += float(pred)

    overall = total/5
    overall = ("%.1f" % overall)
    overall_score.set(overall)
    stop()

def foo():

    print(str(combo.get()))
    hotel = combo.get()
    hotel_fmt = hotel.replace(" ", "+") + "+"
    hotel_fmt = hotel_fmt.replace("&", "")

    print(hotel_fmt)
    import google_scrap as gs

    score_array = gs.google_scrape(hotel_fmt)
    print(len(score_array))
    print(score_array[0])
    pb.start(10)

    hotel_name = "E:\PycharmProjects\MachineL\Hotels Dataset\\" + hotel + ".csv"
    pred = ov.get_average(hotel_name)
    pred = float(pred)
    pred = ("%.1f" % pred)
    display(score_array, pred)


root = Tk()

root.title("Overall Rating")
root.geometry("640x450+600+200")

tkinter.messagebox.showinfo("Welcome", "Welcome to the Machine Learning World")

heading = Label(root, text="The Big Five Score", font=("arial", 20, "bold"), fg="steelblue").pack()

hotel_name_label = Label(root, text="Hotel Name: ", font=("arial", 12), fg="black").place(x=200, y=50)

#hotel_name_entry = Entry(root, textvariable=hotel_name_variable, width=25).place(x=310, y=50)

hotel_name_variable = StringVar()

hotel_list = get_filenames()
combo = ttk.Combobox(root, values=hotel_list)
combo.place(x=310,y=50)
combo.current(1)


# combo1 = ttk.Combobox(root)
# combo1.place(x=310,y=70)
# combo1['values'] = ('1', '2', '3')
# combo1.current(1)

booking_label = Label(root, text="Booking.com: ", font=("arial", 12), fg="black").place(x=50, y=100)
expedia_label = Label(root, text="Expedia: ", font=("arial", 12), fg="black").place(x=200, y=100)
agoda_label = Label(root, text="Agoda: ", font=("arial", 12), fg="black").place(x=300, y=100)
google_label = Label(root, text="Google: ", font=("arial", 12), fg="black").place(x=400, y=100)
my_label = Label(root, text="Predicted: ", font=("arial", 12), fg="black").place(x=500, y=100)

booking = StringVar()
expedia = StringVar()
agoda = StringVar()
google = StringVar()
my = StringVar()

pb = ttk.Progressbar(root, length=640, mode='determinate')
pb.place(x=0, y=200)

booking_score_label = Label(root, textvariable=booking, font=("arial", 12), fg="black")
booking_score_label.place(x=70, y=130)
expedia_score_label = Label(root, textvariable=expedia, font=("arial", 12), fg="black")
expedia_score_label.place(x=220, y=130)
agoda_score_label = Label(root, textvariable=agoda, font=("arial", 12), fg="black")
agoda_score_label.place(x=320, y=130)
google_score_label = Label(root, textvariable=google, font=("arial", 12), fg="black")
google_score_label.place(x=420, y=130)
my_score_label = Label(root, textvariable=my, font=("arial", 12), fg="black")
my_score_label.place(x=520, y=130)


get_value = Button(text="Get Rating", command=foo)
get_value.place(x=300, y=400)

overall_score = StringVar()
overall_score_label = Label(root, textvariable=overall_score, font=("arial", 20))
overall_score_label.place(x=300,y=300)

mainloop()