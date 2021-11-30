from tkinter import Tk
from views import main_view
# starting program from here
window = Tk()
window.title("Varastonhallintajärjestelmä")
ui = main_view.UI(window)
ui.start()
window.mainloop()
