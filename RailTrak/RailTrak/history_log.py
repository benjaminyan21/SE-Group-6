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
    
    img = open('RailTrac_HistoryLog.png', 'rb').read() 

    put_row([put_image(img, width='1000px')])

    put_text('')

    put_row([put_button("Home", onclick=lambda: showMenu(), color='success', outline=True),
             put_button("Logout", onclick=lambda: logoutPage(), color='success', outline=True)])


    f = open("currentUser.txt", "r")
    username = f.read()
    put_text('Welcome, ' + username + '!')
    put_text('Your recent searches:')
    userDB = UserDBM('userDB.txt')
    with use_scope() as newscope:
        userHistory = userDB.readUserHistory(username)
        count = 0
        while (count < userHistory.numSearches):
            put_text('---')
            put_text('Departure: ' + userHistory.departureLocation[count])
            put_text('Arrival: ' + userHistory.arrivalLocation[count])
            minutes = float(userHistory.eta[count])*60
            put_text('ETA: ' + str(minutes) + " minutes")
            count += 1
        put_text('---')

    # Allow the user to filter through their searches by certain criteria
    put_select('in1', ['All', 'New York City', 'Chicago', 'Boston', 'Washington DC'], label='Filter Departure Location')
    put_buttons(['Submit'], lambda _: clear(newscope) and put_historyLog())
    #put_buttons(['Test User History'], lambda _: userDB.writeUserHistory('Austin TX', 'Dallas TX', 0.5))
    cont = True
    while (cont):
        pin_update('in1')
        clear(newscope)
        with use_scope() as writescope:
            if (pin.in1 == "All"):
                count = 0
                while (count < userHistory.numSearches):
                    put_text('---')
                    put_text('Departure: ' + userHistory.departureLocation[count])
                    put_text('Arrival: ' + userHistory.arrivalLocation[count])
                    minutes = float(userHistory.eta[count])*60
                    put_text('ETA: ' + str(minutes) + " minutes")
                    count += 1
                put_text('---')
            else:
                for i, x in enumerate(userHistory.departureLocation):
                    if (x == pin.in1):
                        put_text('Departure: ' + userHistory.departureLocation[i])
                        put_text('Arrival: ' + userHistory.arrivalLocation[i])
                        minutes = float(userHistory.eta[i])*60
                        put_text('ETA: ' + str(minutes) + " minutes")
            pin_wait_change('in1')
            clear(writescope)

        #cont = False
                    #put_select('in1', ['New York City', 'Chicago', 'Boston', 'Washington DC'], label='Filter Departure Location')
            #else:
                #pass
                #clear(newscope)
                #put_select('in1', ['New York City', 'Chicago', 'Boston', 'Washington DC'], label='Filter Departure Location')
                #while True:
                #pin_wait_change('in1')

def put_historyLog():
    f = open("currentUser.txt", "r")
    username = f.read()
    userDB = UserDBM('userDB.txt')
    userHistory = userDB.readUserHistory(username)

    with use_scope() as newscope:
        cont = True
        while (cont):
            put_error("A")
            pin_wait_change('in1')
            pin_update('in1')
            #put_buttons(['Submit'], lambda _: put_historyLog())
            for i, x in enumerate(userHistory.departureLocation):
                put_error("AA")
                put_error(userHistory.departureLocation[i])
                if (x == pin.in1):
                    put_text('Departure: ' + userHistory.departureLocation[i])
                    put_text('Arrival: ' + userHistory.arrivalLocation[i])
                    minutes = float(userHistory.eta[i])*60
                    put_text('ETA: ' + str(minutes) + " minutes")
            cont = False
