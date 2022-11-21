from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from UserDBM import UserDBM
from lloginPage import *

# The main webpage for the history log.
# This page shows the recent searches a user has made, based on
# departure location, departure time, arrival location, and arrival time
def showHistoryLog():
    clear()
    put_row([put_button("Home", onclick=lambda: showMenu(), color='success', outline=True),
             put_button("Logout", onclick=lambda: loginPage(), color='success', outline=True)])
    put_markdown(r""" # RailTrac History Log
    """)
    f = open("currentUser.txt", "r")
    username = f.read()
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