import threading
from views.message_view import MessageView

def show_message(root, msg, message_type):
    message = MessageView(root, msg, message_type)
    message.pack()
    start_time = threading.Timer(5, message.destroy)
    start_time.start()
    