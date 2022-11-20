from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from UserDBM import UserDBM

# Define the login function to show and receive input from user
def showLogin():
    login = input_group("RailTrac Login", [
        input('Username', name='username'),
        input('Password', name='pass', type=PASSWORD)])

    return login['username'], login['pass']

# The main webpage for the history log.
# This page shows the recent searches a user has made, based on
# departure location, departure time, arrival location, and arrival time
def showHistoryLog():
    clear()
    put_row([put_button("Home", onclick=lambda: showMenu(), color='success', outline=True),
             put_button("Logout", onclick=lambda: loginPage(), color='success', outline=True)])
    put_markdown(r""" # RailTrac History Log
    """)
    put_text('Welcome, ' + username + '!')
    put_text('Your recent searches:')
    userDB = UserDBM('userDB.txt')
    with use_scope() as newscope:
        userHistory = userDB.readUserHistory(username)
        put_text('Departure: ' + userHistory.departureLocation +
                 ' (' + userHistory.departureTime + ')')
        put_text('Arrival: ' + userHistory.arrivalLocation +
                 ' (' + userHistory.arrivalTime + ')')

    # Allow the user to filter through their searches by certain criteria
    filterby = select(['Filter Departure Location'], ['Dallas TX', 'Austin TX', 'Houston TX'])
    while (True):
        if (userHistory.departureLocation == filterby):
            clear(newscope)
            with use_scope() as newscope:
                put_text('Departure: ' + userHistory.departureLocation +
                     ' (' + userHistory.departureTime + ')')
                put_text('Arrival: ' + userHistory.arrivalLocation +
                     ' (' + userHistory.arrivalTime + ')')
                filterby = select(['Filter Departure Location'], ['Dallas TX', 'Austin TX', 'Houston TX'])
        else:
            clear(newscope)
            filterby = select(['Filter Departure Location'], ['Dallas TX', 'Austin TX', 'Houston TX'])


# This function shows the main RailTrac menu from which the user can navigate to the history log
def showMenu():
    clear()
    put_markdown(r""" # Welcome to RailTrac!
    RailTrac Menu:
    """)
    put_link('History Log',app='showHistoryLog')
    put_button("Change Locations", onclick=lambda: Selection(), color='success', outline=True)



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

    showMenu()

# Index / homepage of the RailTrac website
def index():
    put_markdown(r""" # RailTrac Homepage
    """)
    put_link('Returning User Login', app='loginPage')

# Start the RailTrac application
start_server([index, loginPage, showHistoryLog], port=80, debug=True, remote_access=True)