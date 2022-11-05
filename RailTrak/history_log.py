from pywebio.input import *
from pywebio.output import put_text
from pywebio import start_server

def userValidation(username, password):
    pass

def show_histlog():
    login = input_group("RailTrac Login", [
        input('Username', name='username'),
        input('Password', name='pass', type=PASSWORD)])



start_server(show_histlog, port=80)