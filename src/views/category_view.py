import tkinter as tk
from tkinter import ttk
from helper_classes.input_validator import InputValidator
from helper_functions import *
from services.import_services import ImportServices

class AddCategoryView:
    def __init__(self, root, state_view_obj, import_view_obf):
        self._state_view_obj = state_view_obj
        self._import_view_obj = import_view_obf
        self._import_services = ImportServices()
        self._root = root
        self._add_category_frame = None
        self._lbl_frame_title = None
        self._lbl_add_category = None
        self._ent_add_category = None
        self._btn_add_category = None

        self._initialize()

    def grid(self, row, col):
        self._add_category_frame.grid(row=row, column=col, sticky=tk.W)

    def _initialize(self):
        self._add_category_frame = tk.Frame(self._root, highlightbackground="gray", highlightthickness=5, bg="#f2f2f2")
        self._lbl_frame_title = tk.Label(self._add_category_frame, text="Lisää uusi kategoria")
        self._lbl_add_category = tk.Label(self._add_category_frame, text="Kategorian Nimi: ")
        self._ent_add_category = tk.Entry(self._add_category_frame)
        self._btn_add_category = tk.Button(self._add_category_frame, text="Lisää Varastoon", command=self._handle_new_category)

        self._lbl_frame_title.grid(row=0, column=1, columnspan=2, sticky=tk.W, padx=5, pady=5)
        self._lbl_add_category.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self._ent_add_category.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self._btn_add_category.grid(row=2, column=1, columnspan=2, sticky=tk.W, padx=5, pady=20)

    def _handle_new_category(self):
        if self._is_empty(self._ent_add_category):
            show_message(self._add_category_frame, "Syötä kateogiran nimi", "ERROR")
        else:
            value = self._ent_add_category.get()
            result = self._import_services.save_category(value)
            if result:
                self._ent_add_category.delete(0, 'end')
                show_message(self._add_category_frame, "Uusi kategoria lisätty!", "SUCCESS")
                self._state_view_obj.update_view()
                self._import_view_obj.update_view()
                self._import_view_obj.grid(1, 1)
                self._state_view_obj.grid(1, 2)
            else:
                show_message(self._add_category_frame, "Uuden kategorian lisääminen ei onnistu!", "WARNING")

    def _is_empty(self, *args):
        for entry in args:
            if InputValidator.is_entry_empty(entry):
                return True
        return False
