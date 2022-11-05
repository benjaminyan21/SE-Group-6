from pywebio.input import *
from pywebio.output import put_text
from pywebio import start_server

def userValidation(username, password):
    with open('users.txt', 'r') as filestream:
        for line in filestream:
            currentLine = line.split(",")
            if (username == currentLine[0] and password == currentLine[1].rstrip()):
                return None
            else: 
                print(username)
                print(currentLine[0])
                print(password)
                print(currentLine[1].rstrip())
        return 'Username or password is incorrect'

def showLogin():
    login = input_group("RailTrac Login", [
        input('Username', name='username'),
        input('Password', name='pass', type=PASSWORD)])

    return login['username'], login['pass']

def show_histlog():
    username, password = showLogin()
    msg = userValidation(username, password)

    while (msg is not None):
        put_text(msg)
        showLogin()

    put_text('ohyeah baby swag')

start_server(show_histlog, port=80, debug=True)