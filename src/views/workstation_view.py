from tkinter import Tk, ttk, Frame, CENTER
import tkinter as tk
from views.import_view import ImportView
from views.state_view import StateView
from views.search_view import SearchView

class WorkstationView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._work_frame = None
        self._import_view = None
        self._state_view = None
        self._search_view = None
        self._btn_logout = None
        self._handle_logout = handle_logout
        self._initialize()

    def pack(self):
        #pack login frame
        self._work_frame.grid(row=0, column=0)
    def destroy(self):
        self._work_frame.destroy()

    def _initialize(self):
        self._work_frame = tk.Frame(self._root, background='white')
        self._import_view = ImportView(self._work_frame)
        self._state_view = StateView(self._work_frame)
        self._search_view = SearchView(self._work_frame)
        self._btn_logout = ttk.Button(
            master=self._work_frame,
             text="Logout",
             command=self._handle_logout
             )

        self._work_frame.place()
        self._btn_logout.grid(row=0, column=0, padx=5, pady=5)
        self._import_view.grid(1, 1)
        self._state_view.grid(1, 2)
        self._search_view.grid(2, 1)
        



