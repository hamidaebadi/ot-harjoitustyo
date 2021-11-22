from tkinter import Tk, ttk, Frame, CENTER

class WorkstationView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._sidebar_import_frame = None
        self._sidebar_export_frame = None
        self._state_frame = None
        self._title_import = None
        self._tilte_export = None
        self._lbl_product_name = None
        self._lbl_product_amount = None
        self._ent_product_name = None
        self._ent_product_amount = None
        self._btn_logout = None
        self._handle_logout = handle_logout

        self._initialize()

    def pack(self):
        #pack login frame
        self._sidebar_import_frame.grid(row=0, column=0, padx=5, pady=5)
        #self._sidebar_export_frame.place()
    
    def destroy(self):
        self._sidebar_import_frame.destroy()

    def _initialize(self):
        self._create_import_frame()
        self._btn_logout = ttk.Button(
            master=self._sidebar_import_frame,
             text="Logout",
             command=self._handle_logout
             )

        self._btn_logout.grid(row=1, column=1, padx=5, pady=5)

    def _create_import_frame(self):
        self._sidebar_import_frame = ttk.Frame(master=self._root)
        self._title_import = ttk.Label(master=self._sidebar_import_frame, text="Tuonti")
        self._lbl_product_name = ttk.Label(master=self._sidebar_import_frame, text="Tuotteen nimi: ")
        self._ent_product_name = ttk.Entry(master=self._sidebar_import_frame)
        self._lbl_product_amount = ttk.Label(master=self._sidebar_import_frame, text="Lukumäärä: ")
        self._ent_product_amount = ttk.Entry(master=self._sidebar_import_frame)


        #komponenttien asettelu
        self._title_import.grid(row=1, column=0, padx=5, pady=5)
        self._lbl_product_name.grid(row=2, column=0, padx=5, pady=5)
        self._ent_product_name.grid(row=2, column=1, padx=5, pady=5)
        self._lbl_product_amount.grid(row=3, column=0, padx=5, pady=5)
        self._ent_product_amount.grid(row=3, column=1, padx=5, pady=5)




