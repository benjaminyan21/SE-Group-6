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
             put_button("Logout", onclick=lambda: logoutPage(), color='success', outline=True)])
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
        minutes = float(userHistory.eta)*60
        put_text('ETA: ' + str(minutes) + " minutes")

    # Allow the user to filter through their searches by certain criteria
    #filterby = 
    put_select('in1', ['Dallas TX', 'Austin TX', 'Houston TX'], label='Filter Departure Location')
    put_buttons(['Submit'], lambda _: put_historyLog())
    put_buttons(['Test User History'], lambda _: userDB.writeUserHistory('Austin TX', 'Dallas TX', 0.5))
    while (get_scope() == newscope):
        put_buttons(['Submit'], lambda _: put_historyLog())
        if (userHistory.departureLocation == pin.in1):
            clear(newscope)
            with use_scope() as newscope:
                put_text('Departure: ' + userHistory.departureLocation)
                put_text('Arrival: ' + userHistory.arrivalLocation)
                minutes = float(userHistory.eta)*60
                put_text('ETA: ' + str(minutes) + " minutes")
                #filterby = 
                put_select('in1', ['Dallas TX', 'Austin TX', 'Houston TX'], label='Filter Departure Location')
        else:
            clear(newscope)
            #filterby = 
            put_select('in1', ['Dallas TX', 'Austin TX', 'Houston TX'], label='Filter Departure Location')
            while True:
                pin_wait_change('in1')

def put_historyLog():
    put_text(pin.in1)