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
        put_text('Departure: ' + userHistory.departureLocation)
        put_text('Arrival: ' + userHistory.arrivalLocation)

        userInfo = input_group("Info", [
            input('Username', name='username')])
        userDB.writeUserHistory(userInfo['username'], ["Austin TX", "Houston TX"])

    # Allow the user to filter through their searches by certain criteria
    filterby = select(['Filter Departure Location'], ['Dallas TX', 'Austin TX', 'Houston TX'])
    while (get_scope() == newscope):
        if (userHistory.departureLocation == filterby):
            clear(newscope)
            with use_scope() as newscope:
                put_text('Departure: ' + userHistory.departureLocation)
                put_text('Arrival: ' + userHistory.arrivalLocation)
                filterby = select(['Filter Departure Location'], ['Dallas TX', 'Austin TX', 'Houston TX'])
        else:
            clear(newscope)
            filterby = select(['Filter Departure Location'], ['Dallas TX', 'Austin TX', 'Houston TX'])