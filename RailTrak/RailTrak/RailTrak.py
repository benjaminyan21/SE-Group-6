﻿from pywebio.input import *
from pywebio.output import put_text
from pywebio import start_server

def TrackGUI():

    data= input_group("Route Information", [
        input('To: ', StartingPoint = 'location', validate=location_check),
        input('From', Destination = 'location', validate=location_check)
        ])

    output.put_text("Here is the route from", StartingPoint, " to", destination)


    
    output.put_image(src, format=None, title='', width=None, height=None, scope=None, position=- 1)


def location_check(data):

    output.put_text("I'm sorry, but the location you entered as not valid")
    


start_server(TrackGUI, port=8080, debug=True)