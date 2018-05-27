# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/
from tkinter import *
import overall_rating as ov
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk, Image

import glob
import os
import time


def setImage(rating):
    star = ['star.png','2star.png','3star.png','4star.png','5star.png']
    if rating==1:
        star = Image.open("C:\dissert\\" + star[0])
    if rating==1:
        star = Image.open("C:\dissert\\" + star[0])
    if rating==1:
        star = Image.open("C:\dissert\\" + star[0])
    if rating==1:
        star = Image.open("C:\dissert\\" + star[0])
    if rating==1:
        star = Image.open("C:\dissert\\" + star[0])
    star = star.resize((150, 30), Image.ANTIALIAS)
    star_img = ImageTk.PhotoImage(star)

    star_label.image = star_img
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

    radio_1.configure(state=NORMAL)
    radio_2.configure(state=NORMAL)
    radio_3.configure(state=NORMAL)


def set_predicted():
    val = v.get()
    if val == 1:
        my.set(clf_score[0])
    if val == 2:
        my.set(clf_score[1])
    if val == 3:
        my.set(clf_score[2])
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class StarPrediction(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

#        tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Star Prediction System")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(0, weight=1)

            #back_img = Image.open("C:\dissert\\home_1.png")
            #background_image = tk.PhotoImage(back_img)
            #back_label = Label(frame, image=background_image)
            #frame.config(bg="blue")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)
        #self.config(bg="black")

        label_f = LabelFrame(self, text="")
        label_f.pack(expand=True, anchor=CENTER)

        # back_img = Image.open("C:\dissert\\home_1.png")
        # background_image = ImageTk.PhotoImage(back_img)
        # back_label = Label(label_f, image=background_image)

        #back_label = Label(label_f, bg="white")
        #back_label.grid(rowspan=2, columnspan=2)
        # back_label.image = background_image

        label = tk.Label(label_f, text="Main Menu", font=LARGE_FONT)
        label.grid(row=0, columnspan =2, pady=50, padx=50, sticky=E+W)

        label.rowconfigure(0, weight=1)
        label.columnconfigure(0, weight=1)

        label_system = tk.Label(label_f, text="Star Prediction System \n Main Menu", font=LARGE_FONT)
        label_system.grid(row=0, columnspan =2, pady=50, padx=50, sticky=E+W+S)

        im1 = Image.open("C:\dissert\\hotel.png")
        im1 = im1.resize((200, 200), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(im1)

        button = tk.Button(label_f, text="Visit Page 1", image=img1, bd=0,
                            command=lambda: controller.show_frame(PageOne))
        button.grid(row=1, sticky=E+W, pady=50, padx=50)
        button.rowconfigure(1, weight=1)
        button.columnconfigure(1, weight=1)
        button.image = img1

        im2 = Image.open("C:\dissert\\graph.png")
        im2 = im2.resize((200, 200), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(im2)

        button3 = tk.Button(label_f, text="Graph Page", image=img2, bd=0,
                             command=lambda: controller.show_frame(PageThree))
        button3.grid(row=1, column=1, sticky=E+W, pady=50, padx=50)
        button3.rowconfigure(1, weight=1)
        button3.columnconfigure(1, weight=1)

        button3.image = img2

        CS_label = Label(label_f, text="Comprehensive Score")
        CS_label.grid(row=1, sticky=E+W+S, pady=50)

        graph_label = Label(label_f, text="Accuracies Graph")
        graph_label.grid(row=1, column=1, sticky=E+W+S, pady=50)

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        heading = Label(self, text="The Big Five Score", font=("arial", 20, "bold"), fg="steelblue").grid(row=0,
                                                                                                          columnspan=4,
                                                                                                          sticky=N + S + E + W)

        labelf_1 = LabelFrame(self, text=" ", padx=10)
        labelf_2 = LabelFrame(self, text="Hotels", padx=10)
        labelf_3 = LabelFrame(self, text="Prediction", padx=10)

        labelf_1.grid(row=1, column=0, sticky=N + S + E + W)
        labelf_1.columnconfigure(1, weight=1)
        labelf_1.rowconfigure(1, weight=1)

        labelf_2.grid(row=1, column=1, sticky=N + S + E + W)
        labelf_2.columnconfigure(1, weight=1)
        labelf_2.rowconfigure(2, weight=1)

        labelf_3.grid(row=1, column=3, sticky=N + S + E + W)
        labelf_3.columnconfigure(1, weight=1)
        labelf_3.rowconfigure(3, weight=1)

        hotel_name_label = Label(labelf_1, text="Hotel Name: ", font=("arial", 12), fg="black").grid(row=0,
                                                                                                     sticky=N + W)

        # hotel_name_entry = Entry(root, textvariable=hotel_name_variable, width=25).place(x=310, y=50)

        hotel_name_variable = StringVar()

        hotel_list = get_filenames()
        global combo
        combo = ttk.Combobox(labelf_1, values=hotel_list)
        combo.grid(row=0, pady=30, sticky=S + E + W)
        combo.current(1)

        global v
        v = IntVar()
        v.set(1)
        global radio_1
        global radio_2
        global radio_3

        radio_1 = Radiobutton(labelf_1, text="Naive Bayes", variable=v, value=1, command=set_predicted, state=DISABLED)
        radio_1.grid(row=1, pady=40, sticky=S + E + W)

        radio_2 = Radiobutton(labelf_1, text="SVM", variable=v, value=2, command=set_predicted, state=DISABLED)
        radio_2.grid(row=2, pady=40, sticky=S + E + W)

        radio_3 = Radiobutton(labelf_1, text="Logistic Regression", variable=v, value=3, command=set_predicted, state=DISABLED)
        radio_3.grid(row=3, pady=40, sticky=S + E + W)

        im1 = Image.open("C:\dissert\\tripadvisor_png.png")
        im1 = im1.resize((90, 60), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(im1)
        tripadvisor_label = Label(labelf_2, image=img1, text="Booking.com: ", font=("arial", 12), fg="black")
        tripadvisor_label.grid(row=0, column=0, padx=10)
        tripadvisor_label.image = img1

        im2 = Image.open("C:\dissert\\expedia_png.png")
        im2 = im2.resize((100, 70), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(im2)
        expedia_label = Label(labelf_2, image=img2, text="Expedia: ", font=("arial", 12), fg="black")
        expedia_label.grid(row=0, column=1, padx=10)
        expedia_label.image = img2

        im3 = Image.open("C:\dissert\\agoda_png.png")
        im3 = im3.resize((90, 30), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(im3)
        agoda_label = Label(labelf_2, image=img3, text="Agoda: ", font=("arial", 12), fg="black")
        agoda_label.grid(row=0, column=2, padx=10)
        agoda_label.image = img3

        im4 = Image.open("C:\dissert\\google_png.png")
        im4 = im4.resize((100, 70), Image.ANTIALIAS)
        img4 = ImageTk.PhotoImage(im4)
        google_label = Label(labelf_2, image=img4, text="Google: ", font=("arial", 12), fg="black")
        google_label.grid(row=0, column=3, padx=10)
        google_label.image = img4

        im5 = Image.open("C:\dissert\\booking_png.png")
        im5 = im5.resize((100, 70), Image.ANTIALIAS)
        img5 = ImageTk.PhotoImage(im5)
        booking_label = Label(labelf_2, image=img5, text="Predicted: ", font=("arial", 12), fg="black")
        booking_label.grid(row=0, column=4, padx=10)
        booking_label.image = img5

        im6 = Image.open("C:\dissert\\Machine_learning_png.png")
        im6 = im6.resize((70, 70), Image.ANTIALIAS)
        img6 = ImageTk.PhotoImage(im6)
        my_label = Label(labelf_3, image=img6, text="Predicted: ", font=("arial", 12), fg="black")
        my_label.grid(row=0, padx=20)
        my_label.image = img6


        global tripadvisor
        global booking
        global expedia
        global agoda
        global google
        global my

        tripadvisor = StringVar()
        booking = StringVar()
        expedia = StringVar()
        agoda = StringVar()
        google = StringVar()
        my = StringVar()

        tripadvisor_score_label = Label(labelf_2, textvariable=tripadvisor, font=("arial", 12), fg="black",
                                        borderwidth=1, relief="solid")
        tripadvisor_score_label.grid(row=1, column=0, pady=10)
        expedia_score_label = Label(labelf_2, textvariable=expedia, font=("arial", 12), fg="black", borderwidth=1,
                                    relief="solid")
        expedia_score_label.grid(row=1, column=1, pady=10)
        agoda_score_label = Label(labelf_2, textvariable=agoda, font=("arial", 12), fg="black", borderwidth=1,
                                  relief="solid")
        agoda_score_label.grid(row=1, column=2, pady=10)
        google_score_label = Label(labelf_2, textvariable=google, font=("arial", 12), fg="black", borderwidth=1,
                                   relief="solid")
        google_score_label.grid(row=1, column=3, pady=10)
        booking_score_label = Label(labelf_2, textvariable=booking, font=("arial", 12), fg="black", borderwidth=1,
                                    relief="solid")
        booking_score_label.grid(row=1, column=4, pady=10)

        my_score_label = Label(labelf_3, textvariable=my, font=("arial", 12), fg="black", borderwidth=2, relief="solid")
        my_score_label.grid(row=1, pady=10)

        get_value = Button(labelf_1, text="Get Rating", command=foo)
        get_value.grid(row=4, pady=10)

        avg_score_label = Label(labelf_2, text="Average Score:", font=("arial", 25))
        avg_score_label.grid(row=2, columnspan=5, sticky=N+E+W, pady=80)
        global overall_score
        overall_score = StringVar()
        overall_score_label = Label(labelf_2, textvariable=overall_score, font=("arial", 20))
        overall_score_label.grid(row=2, columnspan=5, sticky=E + W, pady=10)

        star = Image.open("C:\dissert\\5star.png")
        star = star.resize((150, 30), Image.ANTIALIAS)
        star_img = ImageTk.PhotoImage(star)

        global star_label
        #star_label = Label(labelf_2, image= star_img, font=("arial", 20))
        #star_label.grid(row=2, column=1, columnspan=3, sticky=S+E+W, pady=80)
        #star_label.image = star_img



        im7 = Image.open("C:\dissert\\backbutton.png")
        im7 = im7.resize((70, 70), Image.ANTIALIAS)
        img7 = ImageTk.PhotoImage(im7)

        button1 = tk.Button(self, image=img7, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.grid(row=2, columnspan = 5, pady=10)
        button1.config(bd=0)
        button1.image = img7


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Machine Learning Model \n Accuracies", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()

        im7 = Image.open("C:\dissert\\backbutton.png")
        im7 = im7.resize((70, 70), Image.ANTIALIAS)
        img7 = ImageTk.PhotoImage(im7)

        button1 = tk.Button(self, image=img7, text="Back to Home", bd=0,
                             command=lambda: controller.show_frame(StartPage))
        button1.image = img7
        button1.pack(pady=10)


app = StarPrediction()
#app.wm_attributes('-transparentcolor',app.cget('bg'))
app.mainloop()
