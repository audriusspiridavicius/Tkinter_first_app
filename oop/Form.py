from tkinter import *
from oop.StatusBar import StatusBar
from oop.menu import TopMenu


class Form:

    def __init__(self, window):
        self.window = window
        self.v = StringVar(window)
        self.status = StatusBar(self.window)
        print("testas")

        # self.v.trace("w",self.update_label) #?

        self.label_text = Label(self.window, text="123123123123123", textvariable=self.v)

        # self.v.trace("w", self.update_label) #?

        self.input_name = Entry(self.window)
        self.input_name.config(textvariable=self.v)

        self.label_text.config(text="dsfdsfdsfdsf") #?

        menu = TopMenu(window)
        menu.top_menu()

    def update_label(self,*args):
        pass
        # self.v.set(self.input_name.get())
        # self.status_bar.

        # self.status_bar.update_status_bar()

    def create_form(self):

        label_name = Label(self.window, text="Enter your name")

        button_name = Button(self.window, text="Confirm", command=self.update_status_bar)

        # label_text.config(text=" tra jdhajkf dksajfh hkj")
        button_name.bind("<KP_Enter>", self.update_status_bar)
        # self.input_name.bind("<KP_Enter>", self.update_label)
        # label_text.bind("<KP_Enter>", self.update_label())
        # label_text.bind("<Return>", self.update_label())


        # self.input_name.bind("<Return>", self.update_label)
        # self.input_name.bind("<KeyRelease>", self.update_label)

        # label_text.pack()
        # button_name.pack()

        label_name.grid(row=0, column=0, sticky=E)
        self.input_name.grid(row=0, column=1)
        button_name.grid(row=0, column=2, sticky=E)
        self.label_text.grid(row=1, column=0, columnspan=3)
        # self.status_bar.grid(row=2, column=0, columnspan=3)
        self.window.bind("<Escape>", lambda win:self.window.destroy())

    def update_status_bar(self):

        if len(self.v.get()) > 0:
            self.status.update_status_bar("updated")
        else:
            self.status.update_status_bar("removed")
        # if len(self.status_bar_text.get()) > 0:
        #     self.status_bar.config(text="Sukurta")
        # else:
        #     self.status_bar.config(text="Isvalyta")
        # self.status_bar.config(text=text)
