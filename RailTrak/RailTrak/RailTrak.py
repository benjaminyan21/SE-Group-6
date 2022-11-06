﻿from pywebio.input import *
from pywebio.output import put_text
from pywebio import start_server

def TrackGUI():

    **This is for the Route Information enetered by the User**
    data= input_group("Route Information", [
        input('To: ', StartingPoint = 'StartingPoint', validate=location_check),
        input('From', Destination = 'Destination', validate=location_check)
        ])

    **Some text informing the user that their route is being displayed**
    put_text("Here is the route from", data['StartingPoint'], " to ", data['Destination'])

    **This is not configured yet, but will display the best route for the two entered locations**
    output.put_image(src, format=None, title='', width=None, height=None, scope=None, position=- 1)

    **This is a button that will be on the screen, it is going to display the route information when clicked**
    put_button("Route Information", onclick=lambda: toast(RouteInformation), color='success', outline=True)

    put_button("Toggle Map", onclick=lambda: toast("Will toggle change in map type"), color='success', outline=True)

    put_button("Zoom in", onclick=lambda: toast("Will zoom in on map"), color='success', outline=True)

    put_button("Zoom out", onclick=lambda: toast("Will zoom out on map"), color='success', outline=True)



**This is for validating the entered locations as we are having constrictions on what cities you can user, ect.**
def location_check(data):

    if len(data['StartingPoint']) != 'ValidLocation':
        return('StartingPoint', ' is not a Valid Location')


    if len(data['Destination']) != 'ValidLocation':
        return('Destination', ' is not a Valid Location')

def RouteInformation(data):

    **going to need the database to be configured for this, and for most of the buttons i think**
    popup('Route Information', "Information for a route from", 'StartingPoint', "to", 'Destination')




    


**this is for the server**
start_server(TrackGUI, port=8080, debug=True)