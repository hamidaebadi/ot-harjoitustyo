import tkinter as tk
from tkinter import ttk
from helper_classes.input_validator import InputValidator
from helper_functions import *
from services.storage_services import Storage
class SearchView:
    def __init__(self, root):
        self._storage = Storage()
        self._root = root
        self._search_frame = None
        self._lbl_frame_title = None
        self._lbl_search = None
        self._ent_search = None
        self._btn_search = None

        #result area components
        self._lbl_result_area = None
        self._lbl_result_name = None
        self._lbl_result_quantity = None
        self._lbl_result_QRcode = None
        self._btn_remove_product = None


        self._initialize()

    def grid(self, row, col):
        self._search_frame.grid(row=row, column=col, sticky=tk.W)

    def _initialize(self):
        self._search_frame = tk.Frame(self._root, highlightbackground="gray", highlightthickness=5, bg="#f2f2f2")
        self._lbl_frame_title = tk.Label(self._search_frame, text="Etsi Tuote")
        self._lbl_search = tk.Label(self._search_frame, text="Nimi tai QR-koodi: ")
        self._ent_search = tk.Entry(self._search_frame)
        self._btn_search = tk.Button(self._search_frame, text="Löydä tuote", command=self._handle_search)

        self._lbl_frame_title.grid(row=0, column=1, columnspan=2, sticky=tk.W, padx=5, pady=5)
        self._lbl_search.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self._ent_search.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self._btn_search.grid(row=2, column=1, columnspan=2, sticky=tk.W, padx=5, pady=20)

    def _handle_search(self):
        if self._is_empty(self._ent_search):
            show_message(self._search_frame, "Syötä joko nimi tai QR-koodi", "ERROR")
        else:
            value = self._ent_search.get()
            product = self._storage.search_product(value)
            if product:
                self._show_result_area(product.product_name, product.product_quantity, product.product_qr_code)
            else:
                show_message(self._search_frame, "Tuote ei löydy!", "WARNING")

    def _is_empty(self, *args):
        for entry in args:
            if InputValidator.is_entry_empty(entry):
                return True
        return False

    def _show_result_area(self, name, quantity, qr_code):
        self._initialize_result_area(name, quantity, qr_code)

    def _initialize_result_area(self, name, quantity, qr_code):
        self._lbl_result_area = tk.Label(self._search_frame, text="Löydetty Tuote", fg='green')
        self._lbl_result_name = tk.Label(self._search_frame, text=name)
        self._lbl_result_quantity = tk.Label(self._search_frame, text=quantity)
        self._lbl_result_QRcode = tk.Label(self._search_frame, text=qr_code)
        self._btn_remove_product = tk.Button(self._search_frame, text="Remove Product")

        self._lbl_result_area.grid(row=3, column=1, columnspan=2, padx=5, sticky=tk.W)
        self._lbl_result_name.grid(row=4, column=0, pady=5)
        self._lbl_result_quantity.grid(row=4, column=1, pady=5)
        self._lbl_result_QRcode.grid(row=4, column=2, pady=5)
        self._btn_remove_product.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)