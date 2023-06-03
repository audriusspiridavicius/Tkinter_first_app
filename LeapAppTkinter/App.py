from tkinter import Tk, StringVar, IntVar
from tkinter import ttk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
import calendar

class App(Tk):

    def __init__(self):
        super().__init__()

        self.year_input_field_value = IntVar()

        self.appFrame = ttk.Frame(self)

        self.geometry("300x300+250+150")

        self.label = Label(self.appFrame, anchor="w", text="Please enter a Year")
        self.year_input_field = Entry(self.appFrame, textvariable=self.year_input_field_value)

        #clickable button that call a function

        self.confirm_button = Button(self.appFrame, anchor="w", command=self.click_confirm_button)

    def click_confirm_button(self):

        is_leap = self.check_is_leap_year()

        if is_leap:
            pass
        else:
            pass

    def check_is_leap_year(self):

        return calendar.isleap(int(self.year_input_field_value.get()))

    def _display_elements(self):

        self.label.grid(self.frame,)


