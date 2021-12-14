from tkinter import Tk, ttk, Frame, OptionMenu, StringVar
import tkinter as tk
from helper_functions import *
from helper_classes.input_validator import InputValidator
from services.import_services import ImportServices
from services.storage_services import Storage

class ImportView:
    def __init__(self, root, state_view_obj):
        self._root = root
        self._storage = Storage()
        self._import_frame = None
        self._state_view_obj = state_view_obj
        self._lbl_title = None
        self._lbl_product_name = None
        self._lbl_product_amount = None
        self._lbl_product_category = None
        self._ent_product_name = None
        self._ent_product_amount = None
        self._lbl_product_QR = None
        self._ent_product_QR = None
        self._lbl_list_box = None
        self._list_box = None
        self._btn_add_product = None
        self._categories = []
        self._variable = None
        self._selected_category = None

        self._initialize()

 
    def destroy(self):
        self._import_frame.destroy()

    def grid(self, row, col):
        self._import_frame.grid(row=row, column=col)

    def _initialize(self):
        self.__initialize_all_categories()
        self._import_frame = tk.Frame(self._root, highlightbackground="gray", highlightthickness=5, bg="#f2f2f2")
        self._lbl_title = tk.Label(self._import_frame, text="Lisää tuote")
        self._lbl_product_name = tk.Label(self._import_frame, text="Tuotteen Nimi: ")
        self._ent_product_name = tk.Entry(self._import_frame)
        self._lbl_product_amount = tk.Label(self._import_frame, text="Lukumäärä: ")
        self._lbl_product_QR = tk.Label(self._import_frame, text="QR-code: ")
        self._ent_product_QR = tk.Entry(self._import_frame)
        self._ent_product_amount = tk.Entry(self._import_frame)
        self._lbl_list_box = tk.Label(self._import_frame, text="Valitse kategoria: ")
        self._variable = StringVar()
        self._variable.set(self._categories[0])
        self._list_box = OptionMenu(self._import_frame, self._variable, *self._categories, command=self._get_optionMenu_value)
        self._btn_add_product = tk.Button(master=self._import_frame, text="Lisää varastoon", command=self._handle_add_product_btn)

        #place widgets
        self._lbl_title.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky=tk.W)
        self._lbl_product_name.grid(row=1, column=0,  padx=5, pady=5, sticky=tk.W)
        self._ent_product_name.grid(row=1, column=1,  padx=5, pady=5, sticky=tk.W)
        self._lbl_product_amount.grid(row=2, column=0,  padx=5, pady=5, sticky=tk.W)
        self._ent_product_amount.grid(row=2, column=1,  padx=5, pady=5, sticky=tk.W)
        self._lbl_product_QR.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self._ent_product_QR.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        self._lbl_list_box.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self._list_box.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        self._btn_add_product.grid(row=5, column=1, columnspan=2, sticky=tk.W)

    def __initialize_all_categories(self):
        for cage in self._storage.get_cages():
            self._categories.append(cage.cage_name)

    def _handle_add_product_btn(self):
        incorrect_input = self._is_empty(
            self._ent_product_name,
            self._ent_product_amount,
            self._ent_product_QR
        )
        if incorrect_input:
            show_message(self._root, "Kentät eivät saa olla tyhjä", "ERROR")
        else:
            name = self._ent_product_name.get()
            quantity = self._ent_product_amount.get()
            QR_code = self._ent_product_QR.get()
            category = self._selected_category

            save_product = ImportServices()
            result = save_product.save_product(name, category, QR_code, quantity)
            if result:
                self._erase_iputs()
                show_message(self._import_frame, "Tuote lisätty!", "SUCCESS")
                self._state_view_obj.update_view()
                self._state_view_obj.grid(1, 2)
    

    def _get_optionMenu_value(self, choice):
        choice = self._variable.get()
        self._selected_category = choice

    def _erase_iputs(self):
        self._ent_product_name.delete(0, 'end')
        self._ent_product_amount.delete(0, 'end')
        self._ent_product_QR.delete(0, 'end')
        
    def _is_empty(self, *args):
        #check if inputs are not empty
        for entry in args:
            if InputValidator.is_entry_empty(entry):
                return True
        return False