from tkinter import Tk
from oop.Form import Form
from oop.menu import TopMenu
from oop.StatusBar import StatusBar
window = Tk()

form = Form(window)
form.create_form()


window.mainloop()