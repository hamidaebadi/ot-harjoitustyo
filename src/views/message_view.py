from tkinter import Tk, ttk, Frame, CENTER
import tkinter as tk
class MessageView:
    def __init__(self,root, content, msg_type):
        self._root = root
        self._message = content
        self._frame = None
        self._lbl_message = None
        self._message_type = msg_type
        self._message_color = None
        self._initialize()

    def pack(self):
        self._frame.place(relx=.5, rely=.6,anchor= CENTER)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._detect_message_type(self._message_type)
        self._frame = ttk.Frame(self._root)
        self._lbl_message = tk.Label(self._frame, text=self._message, fg=self._message_color)
        self._lbl_message.pack()

    def _detect_message_type(self, type):
        if type == "ERROR":
            self._message_color = 'red'
        elif type == "WARNING":
            self._message_color = 'orange'
        elif type == "SUCCESS":
            self._message_color = 'green'

    