from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from UserDBM import UserDBM

def showLogin():
    login = input_group("RailTrac Login", [
        input('Username', name='username'),
        input('Password', name='pass', type=PASSWORD)])

    return login['username'], login['pass']

def showHistoryLog():
    put_button("Home", onclick=lambda: showMenu(), color='success', outline=True)
    put_markdown(r""" # RailTrac History Log
    Your recent searches:
    """)
    userDB = UserDBM('userDB.txt')
    userHistory = userDB.readUserHistory(username)
    put_text('Departure: ' + userHistory.departureLocation +
             ' (' + userHistory.departureTime + ')')
    put_text('Arrival: ' + userHistory.arrivalLocation +
             ' (' + userHistory.arrivalTime + ')')

def showMenu():
    clear()
    put_markdown(r""" # Welcome to RailTrac!
    RailTrac Menu:
    """)
    put_link('History Log',app='showHistoryLog')

def loginPage():
    global username
    username, password = showLogin()
    userDB = UserDBM('userDB.txt')
    msg = userDB.validate(username, password)

    while (msg is not None):
        clear()
        put_error(msg)
        username, password = showLogin()
        msg = userDB.validate(username, password)

    showMenu()

def index():
    put_markdown(r""" # RailTrac Homepage
    """)
    put_link('Returning User Login', app='loginPage')

start_server([index, loginPage, showHistoryLog], port=80, debug=True, remote_access=True)