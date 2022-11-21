from pywebio.input import *
from pywebio.output import *
from UserDBM import UserDBM

# This function gets the login from the user and validates it against the database
def loginPage():
    clear()
    global username
    username, password = showLogin()
    userDB = UserDBM('userDB.txt')
    msg = userDB.validate(username, password)

    while (msg is not None):
        clear()
        put_error(msg)
        username, password = showLogin()
        msg = userDB.validate(username, password)

    f = open("currentUser.txt", "w")
    f.write(username)
    f.close()
    showMenu()

# Define the login function to show and receive input from user
def showLogin():
    login = input_group("RailTrac Login", [
        input('Username', name='username'),
        input('Password', name='pass', type=PASSWORD)])

    return login['username'], login['pass']

# This function shows the main RailTrac menu from which the user can navigate to the history log
def showMenu():
    clear()
    put_markdown(r""" # Welcome to RailTrac!
    RailTrac Menu:
    """)
    put_link('Find a Route',app='Selection')
    put_text('')
    put_link('History Log',app='showHistoryLog')