from tkinter import *


class TopMenu:
    def __init__(self, window):
        self.window = window
        # self.text_input:Entry = self.window.nametowidget("input_name")

        self.text_input: Entry = self.window.nametowidget("!entry")
        self.previos_value = ""

        # self.text_input:Entry = self.window.nametowidget(".Entry")

    def top_menu(self):
        # menu = Menu(self.window)
        meniu = Menu(self.window)
        self.window.config(menu=meniu)
        submeniu = Menu(meniu, tearoff=0)
        # submeniu = Menu(meniu)

        # meniu.
        meniu.add_cascade(label="Meniu", menu=submeniu)
        submeniu.add_command(label="Isvalyti", command=self.clear_value)
        submeniu.add_command(label="Atkurti puslapi", command=self.return_previos_value)
        submeniu.add_separator()
        submeniu.add_command(label="Iseiti", command=self.close_windows)

    def clear_value(self):
        print(f"text input {self.text_input}")
        self.previos_value = self.text_input.get()
        self.text_input.delete(0, END)

    def return_previos_value(self):
        self.text_input.delete(0, END)
        self.text_input.insert(0,self.previos_value)

    def close_windows(self):
        self.window.destroy()