from tkinter import Tk, ttk, Frame, CENTER
class MessageView:
    def __init__(self,root, content):
        self._root = root
        self._message = content
        self._frame = None
        self._lbl_message = None

        self._initialize()

    def pack(self):
        self._frame.place(relx=.5, rely=.5,anchor= CENTER)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._lbl_message = ttk.Label(self._frame, text=self._message)
        self._lbl_message.pack()

    