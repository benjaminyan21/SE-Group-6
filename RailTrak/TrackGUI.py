from pywebio import *
from pywebio.output import *
from pywebio.input import *
from pywebio.output import put_text
#from history_log import showHistoryLog
from UserDBM import UserDBM
from pywebio import start_server


def Selection():

    put_markdown(r""" # RailTrac Selection Page
""")


    
    #StartingPoint = select('Starting Location?', name = ['Denver', 'Chicago'])
    #Destination = select('Destination?', name = ['NYC', 'Boston'])
    StartingPoint = radio("Starting Location?", options=['Denver', 'Chicago', 'Boston', 'NYC'])
    Destination = radio("Destination", options=['Denver', 'Chicago', 'Boston', 'Washington DC'])

    #return data['StartingPoint'], data['Destination']

    #put_link('Find fastest route?', app='TrackGUI')

    TrackGUI(StartingPoint, Destination)


    #return StartingPoint['StartingPoint'], Destination['Destination']

def SelectionPage():
    clear()
    global StartingPoint
    StartingPoint, Destination = Selection

    data= input_group("Route Information", [
        input('StartingPoint', name = 'StartingPoint'),
        input('Destination', name = 'Destination')
        ])

    TrackGUI




def TrackGUI(StartingPoint, Destination):

    clear()

    put_markdown(r""" # RailTrac Route Display
""")
    put_row([put_button("Home", onclick=lambda: showMenu(), color='success', outline=True),
             put_button("Logout", onclick=lambda: loginPage(), color='success', outline=True)])

    put_text('')

    #Some text informing the user that their route is being displayed
    put_text("Here is the route from " + StartingPoint + " to " + Destination)


    put_text('')

    #image of west coast
    #put_image('https://www.up.com/cs/groups/public/@uprr/@corprel/documents/digitalmedia/omhq17a129812003487.gif')

    put_image('https://www.railwayage.com/wp-content/uploads/2021/04/Amtrak-Map-1024x576.jpg')
    
    
    #put_image('https://understandingsocietyglobaledition.files.wordpress.com/2011/08/photo-12.png')

    put_markdown(r""" # Map Features
""")

    put_row([put_button("Toggle Map", onclick=lambda: toast("will change map type"), color='success', outline=True),
             put_button("Route Information", onclick=lambda: DisplayRouteInfo(StartingPoint, Destination), color='success', outline=True),
             put_button("Zoom In", onclick=lambda: ZoomIn(StartingPoint, Destination), color='success', outline=True),
             put_button("Zoom Out", onclick=lambda: toast("You can not zoom out"), color='success', outline=True)])




def DisplayRouteInfo(StartingPoint, Destination):

    popup('Route information', 'Information')


def ZoomIn(StartingPoint, Destination):

    clear()

    put_markdown(r""" # RailTrac Route Display
""")
    put_row([put_button("Home", onclick=lambda: showMenu(), color='success', outline=True),
             put_button("Logout", onclick=lambda: loginPage(), color='success', outline=True)])

    put_text('')

    #Some text informing the user that their route is being displayed
    put_text("Here is the route from " + StartingPoint + " to " + Destination)


    put_text('')

    #image of west coast
    #put_image('https://www.up.com/cs/groups/public/@uprr/@corprel/documents/digitalmedia/omhq17a129812003487.gif')

    if StartingPoint == 'Boston':
       if Destination == 'Washington DC':
        put_image('https://www.amtrak.com/content/dam/projects/dotcom/english/public/images/nec/northeast-corridor-map.jpg/_jcr_content/renditions/original')

    #Big image
    #put_image('https://understandingsocietyglobaledition.files.wordpress.com/2011/08/photo-12.png')

    put_markdown(r""" # Map Features
""")

    put_row([put_button("Toggle Map", onclick=lambda: toast("will change map type"), color='success', outline=True),
             put_button("Route Information", onclick=lambda: DisplayRouteInfo(StartingPoint, Destination), color='success', outline=True),
             put_button("Zoom In", onclick=lambda: ZoomIn(StartingPoint, Destination), color='success', outline=True),
             put_button("Zoom Out", onclick=lambda: TrackGUI(StartingPoint, Destination), color='success', outline=True)])


    return()

# Start the RailTrac application
start_server([Selection], port=80, debug=True, remote_access=True)


