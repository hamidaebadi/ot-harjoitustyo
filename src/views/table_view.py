from tkinter import Tk, ttk, Frame
import tkinter as tk

class Table:
    def __init__(self, root):
        self._root = root
        self._table_frame = None


        self._intialize_table()

    def set_headers(self, headers):
        col = 0
        row = 0
        for header in headers:
            lbl = tk.Label(master=self._table_frame, text=header)
            lbl.grid(row=row, column=col, padx=60)
            col += 1

    def create_table(self, row, column, data):
        for i in range(row):
            for j in range(column):
                l1 = tk.Label(master=self._table_frame, text=data[i].product_name)
                l2 = tk.Label(master=self._table_frame, text=data[i].product_quantity)
                l3 = tk.Label(master=self._table_frame, text=data[i].product_qr_code)
                l1.grid(row=i+1, column=0, pady=5)
                l2.grid(row=i+1, column=1, pady=5)
                l3.grid(row=i+1, column=2, pady=5)

    def _intialize_table(self):
        self._table_frame = Frame(self._root)

    def pack(self):
        self._table_frame.pack(fill='both', expand=True)

        
