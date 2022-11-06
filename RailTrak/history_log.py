from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from UserDBM import UserDBM

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
    userDB = UserDBM('userDB.txt')
    #msg = userValidation(username, password)
    msg = userDB.validate(username, password)

    while (msg is not None):
        clear()
        put_error(msg)
        username, password = showLogin()
        msg = userDB.validate(username, password)

    clear()
    put_text('Welcome to RailTrac!')

start_server(show_histlog, port=80, debug=True)