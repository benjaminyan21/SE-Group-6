from pywebio import *
from pywebio.output import *
from pywebio.input import *
from pywebio.output import put_text
from pywebio import start_server

#This page is going to represent the GUI for finding the quickest route.

def TrackGUI():

    #This is for the Route Information enetered by the User
    #Validation is also run to make sure the locations entered are valid, but I'm debating on a drop down menu to make it easier
    data= input_group("Route Information", [
        input('To: ', StartingPoint = 'StartingPoint', validate=location_check),
        input('From', Destination = 'Destination', validate=location_check)
        ])

    #Some text informing the user that their route is being displayed
    put_text("Here is the route from", data['StartingPoint'], " to ", data['Destination'])

    #This is not configured yet, but will display the best route for the two entered locations/ Right here is an exmaple of the map
    put_image('https://understandingsocietyglobaledition.files.wordpress.com/2011/08/photo-12.png')

    #This is a button that will be on the screen, it is going to display the route information when clicked
    put_button("Route Information", onclick=lambda: toast(RouteInformation), color='success', outline=True)

    put_button("Toggle Map", onclick=lambda: toast("Will toggle change in map type"), color='success', outline=True)

    put_button("Zoom in", onclick=lambda: toast("Will zoom in on map"), color='success', outline=True)

    put_button("Zoom out", onclick=lambda: toast("Will zoom out on map"), color='success', outline=True)




#This is for validating the entered locations as we are having constrictions on what cities you can user, ect.
def location_check(data):

    if len(data['StartingPoint']) != 'location':
        #return('StartingPoint', ' is not a Valid Location')
        return()


    if len(data['Destination']) != 'location':
        return()
        #return('Destination', ' is not a Valid Location')

#This is the popup that will be triggered by the 'Route Information button'.
def RouteInformation():

    #going to need the database to be configured for this, and for most of the buttons i think
    popup("Route Information: Information for a route from Starting Point to Destination")


#def ToggleMap():
    

#Actually, will combine zoom in and out so that if zoomed in can only go out vise versa
#def ZoomIn():
#def ZoomOut():







    


#this is for the server
start_server(TrackGUI, port=8080, debug=True)
