import tkinter as tk
from tkinter import ttk, Tk, Frame
from views.scrollable_frame_view import ScrollableFrame
from views.table_view import Table
from services.storage_services import Storage

class StateView:
    def __init__(self, root):
        self._root = root
        self._notebook = None
        self._storage_services = Storage()
        

        self._initialize()
    
    def _initialize(self):
        self._notebook = ttk.Notebook(self._root, height=750, width=800)
        #create tabs
        self._create_tabs()

    def _create_tabs(self):
        tabs = self._storage_services.get_cages()
        headers = ["Tuotteen Nimi", "Lukumäärä", "QR-koodi"]
        if tabs:
            for tab in tabs:
                frame_tab = ScrollableFrame(self._notebook)
                data_table = Table(frame_tab)
                data_table.set_headers(headers)
                items = self._storage_services.get_stored_products(tab.cage_name)
                data_table.create_table(len(items), 3, items)
                data_table.pack()
                frame_tab.pack(fill='both', expand=True)
                self._notebook.add(frame_tab, text=tab.cage_name)

    def grid(self, row, col):
        self._notebook.grid(row=row, column=col, rowspan=3, padx=10)
