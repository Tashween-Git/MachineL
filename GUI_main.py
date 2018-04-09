from tkinter import *
import overall_rating as ov
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk, Image

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

def display(score_array, pred):

    tripadvisor.set(score_array[0])
    expedia.set(score_array[2])
    agoda.set(score_array[3])
    google.set(score_array[4])
    booking.set(score_array[1])

    my.set(pred[0])
    total = 0

    for x in score_array:
        total += float(x)

    # total += float(pred)

    overall = total/5
    overall = ("%.1f" % overall)
    overall_score.set(overall)

global clf_score
clf_score = []

def foo():

    print(str(combo.get()))
    hotel = combo.get()
    hotel_fmt = hotel.replace(" ", "+") + "+"
    hotel_fmt = hotel_fmt.replace("&", "")
    hotel_fmt = hotel_fmt.replace("’", "")

    print(hotel_fmt)
    import google_scrap as gs

    score_array = gs.google_scrape(hotel_fmt)
    print(len(score_array))
    print(score_array[0])

    hotel_name = "E:\PycharmProjects\MachineL\Hotels Dataset\\" + hotel + ".csv"
    pred = ov.get_average(hotel_name)

    for i in pred:
        clf_score.append(i)

    display(score_array, pred)


def set_predicted():
    val = v.get()
    if val == 1:
        my.set(clf_score[0])
    if val == 2:
        my.set(clf_score[1])
    if val == 3:
        my.set(clf_score[2])

root = Tk()

heading = Label(root, text="The Big Five Score", font=("arial", 20, "bold"), fg="steelblue").grid(row=0, columnspan=4, sticky=N+S+E+W)


labelf_1 = LabelFrame(root, text=" ", padx=10)
labelf_2 = LabelFrame(root, text="Hotels", padx=10)
labelf_3 = LabelFrame(root, text="Prediction", padx=10)


labelf_1.grid(row=1, column=0, sticky=N+S+E+W)
labelf_1.columnconfigure(1, weight=1)
labelf_1.rowconfigure(1, weight =1)

labelf_2.grid(row=1, column=1, sticky=N+S+E+W)
labelf_2.columnconfigure(1, weight=1)
labelf_2.rowconfigure(2, weight =1)

labelf_3.grid(row=1, column=3, sticky=N+S+E+W)
labelf_3.columnconfigure(1, weight=1)
labelf_3.rowconfigure(3, weight =1)


hotel_name_label = Label(labelf_1, text="Hotel Name: ", font=("arial", 12), fg="black").grid(row=0, sticky=N+W)

#hotel_name_entry = Entry(root, textvariable=hotel_name_variable, width=25).place(x=310, y=50)

hotel_name_variable = StringVar()

hotel_list = get_filenames()
combo = ttk.Combobox(labelf_1, values=hotel_list)
combo.grid(row=0,pady=30, sticky=S+E+W)
combo.current(1)


v = IntVar()
v.set(1)
radio_1 = Radiobutton(labelf_1, text="Naive Bayes", variable=v, value =1, command=set_predicted)
radio_1.grid(row=1,pady=40, sticky=S+E+W)
radio_2 = Radiobutton(labelf_1, text="SVM", variable=v, value =2, command=set_predicted)
radio_2.grid(row=2,pady=40, sticky=S+E+W)
radio_3 = Radiobutton(labelf_1, text="Logistic Regression", variable=v, value =3, command=set_predicted)
radio_3.grid(row=3,pady=40, sticky=S+E+W)

im1 = Image.open("C:\dissert\\tripadvisor_png.png")
im1= im1.resize((90,60), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(im1)

tripadvisor_label = Label(labelf_2, image= img1, text="Booking.com: ", font=("arial", 12), fg="black").grid(row=0, column=0, padx=10)

im2 = Image.open("C:\dissert\\expedia_png.png")
im2 = im2.resize((100,70), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(im2)
expedia_label = Label(labelf_2, image= img2, text="Expedia: ", font=("arial", 12), fg="black").grid(row=0, column=1, padx=10)

im3 = Image.open("C:\dissert\\agoda_png.png")
im3 = im3.resize((90,30), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(im3)
agoda_label = Label(labelf_2, image= img3, text="Agoda: ", font=("arial", 12), fg="black").grid(row=0, column=2, padx=10)

im4 = Image.open("C:\dissert\\google_png.png")
im4 = im4.resize((100,70), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(im4)
google_label = Label(labelf_2, image= img4, text="Google: ", font=("arial", 12), fg="black").grid(row=0, column=3, padx=10)

im5 = Image.open("C:\dissert\\booking_png.png")
im5 = im5.resize((100,70), Image.ANTIALIAS)
img5 = ImageTk.PhotoImage(im5)
booking_label = Label(labelf_2, image= img5, text="Predicted: ", font=("arial", 12), fg="black").grid(row=0, column=4, padx=10)


im6 = Image.open("C:\dissert\\Machine_learning_png.png")
im6 = im6.resize((70,70), Image.ANTIALIAS)
img6 = ImageTk.PhotoImage(im6)
my_label = Label(labelf_3, image= img6, text="Predicted: ", font=("arial", 12), fg="black").grid(row=0, padx=20)

tripadvisor = StringVar()
booking = StringVar()
expedia = StringVar()
agoda = StringVar()
google = StringVar()
my = StringVar()


tripadvisor_score_label = Label(labelf_2, textvariable=tripadvisor, font=("arial", 12), fg="black", borderwidth=1, relief="solid")
tripadvisor_score_label.grid(row=1, column=0, pady=10)
expedia_score_label = Label(labelf_2, textvariable=expedia, font=("arial", 12), fg="black", borderwidth=1, relief="solid")
expedia_score_label.grid(row=1, column=1, pady=10)
agoda_score_label = Label(labelf_2, textvariable=agoda, font=("arial", 12), fg="black", borderwidth=1, relief="solid")
agoda_score_label.grid(row=1, column=2, pady=10)
google_score_label = Label(labelf_2, textvariable=google, font=("arial", 12), fg="black", borderwidth=1, relief="solid")
google_score_label.grid(row=1, column=3, pady=10)
booking_score_label = Label(labelf_2, textvariable=booking, font=("arial", 12), fg="black", borderwidth=1, relief="solid")
booking_score_label.grid(row=1, column=4, pady=10)

my_score_label = Label(labelf_3, textvariable=my, font=("arial", 12), fg="black", borderwidth=2, relief="solid")
my_score_label.grid(row=1, pady=10)

get_value = Button(labelf_1, text="Get Rating", command=foo)
get_value.grid(row=4,pady=10)

overall_score = StringVar()
overall_score_label = Label(labelf_2, textvariable=overall_score, font=("arial", 20))
overall_score_label.grid(row=2, columnspan = 5, sticky=N+S+E+W, pady=10)



root.mainloop()