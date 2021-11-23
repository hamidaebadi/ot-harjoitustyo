from tkinter import Tk, ttk, Frame, CENTER
class LoginView:
    def __init__(self, root, handle_workstation):
        self._root = root
        self._frame = None
        self._lbl_username = None
        self._lbl_password = None
        self._ent_username = None
        self._ent_password = None
        self._handle_workstation = handle_workstation

        self._initialize()

    def pack(self):
        #pack login frame
        self._frame.place(relx=.5, rely=.5,anchor= CENTER)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Kirjaudu Sisään")
        self._lbl_username = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._lbl_password = ttk.Label(master=self._frame, text="Salasana")
        self._ent_username = ttk.Entry(master=self._frame)
        self._ent_password = ttk.Entry(master=self._frame)
        btn_login = ttk.Button(master=self._frame,
         text="Kirjaudu sisään",
         command=lambda: self._handle_workstation(self._ent_username.get(), self._ent_password.get())
         )

        label.grid(row=0, column=1, padx=5, pady=5)
        self._lbl_username.grid(row=1, column=0, padx=5, pady=5)
        self._ent_username.grid(row=1, column=1, padx=5, pady=5)
        self._lbl_password.grid(row=2, column=0, padx=5, pady=5)
        self._ent_password.grid(row=2, column=1, padx=5, pady=5)
        btn_login.grid(row=3, column=1, padx=5, pady=5)

    
