import tkinter
from tkinter import *


class StatusBar:
    def __init__(self, window, *args):
        self.window = window
        # self.status_bar_text = tkinter.StringVar(window)
        self.status_bar = Label(window, text="", relief=FLAT, anchor="e")
        # self.status_bar_text.trace('w', self.update_status_bar)

        self.status_bar.grid(row=2, columnspan=3, sticky=W + E) # ??????????????????????

    def update_status_bar(self,text):

        self.status_bar.config(text=text)
