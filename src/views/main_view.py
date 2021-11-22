from views.login_view import LoginView
from views.workstation_view import WorkstationView
from services.login_services import LoginServices
class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._root.minsize(1200, 800)
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._handle_login)
        self._current_view.pack()

    def _show_workstation_view(self):
         self._hide_current_view()
         self._current_view = WorkstationView(self._root, self._handle_logout)
         self._current_view.pack()

    def _handle_login(self, username, password):
        loginSession = LoginServices()
        loggedIn = loginSession.login(username, password)
        if loggedIn:
            self._show_workstation_view()
        else:
            print("Wrong credentials")
            #self._show_message(message)

    def _handle_logout(self):
        self._show_login_view()


