from pywebio import *
from pywebio.output import *
from pywebio.input import *
from pywebio.output import put_text
#from history_log import showHistoryLog
from UserDBM import UserDBM
from pywebio import start_server
from lloginPage import *
import TrackDatabase as trackDB
from Path import Path





def Selection():

    clear()

    put_markdown(r""" # RailTrac Selection Page
""")

    
    #StartingPoint = select('Starting Location?', name = ['Denver', 'Chicago'])
    #Destination = select('Destination?', name = ['NYC', 'Boston'])

    cities = ['New York City', 'Chicago', 'Boston', 'Washington DC']

    StartingPoint = radio("Starting Location?", options= cities)
    
    cities.remove(StartingPoint)
    Destination = radio("Destination", options= cities)

    #return data['StartingPoint'], data['Destination']

    put_link('Find fastest route?', app='TrackGUI')

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

    img = open('RailTrac.png', 'rb').read()
    map_original = open('zoom_out_image.png', 'rb').read()

    put_row([put_image(img, width='100px'),put_markdown(r""" # RailTrac Route Display
""")], size='35% 65%')


    put_row([put_button("Home", onclick=lambda: showMenu(), color='success', outline=True),
             put_button("Logout", onclick=lambda: loginPage(), color='success', outline=True),
             put_button("Change Locations", onclick=lambda: Selection(), color='success', outline=True)])

    userDB = UserDBM('userDB.txt')
    db = trackDB.TrackDB()
    db.initialize();
    
    path = db.shortestPath([StartingPoint, Destination])
    userDB.writeUserHistory(StartingPoint, Destination, path.eta)

    put_text('')

    put_row([put_text(''),
             put_text(StartingPoint + " to " + Destination).style('font-size: 35px')], size='25% 75%')



    put_text('')

    put_row([put_text(''),
             put_text("ETA is", path.eta, "hours").style('color: red; font-size: 20px')], size='35% 65%')


    #Some text informing the user that their route is being displayed

    s = ''
    for i in range(len(path.route)-1):
        s += path.route[i] + ', '
    s += path.route[len(path.route)-1]

    put_text("The route from " + StartingPoint + " to " + Destination + " is: " + s).style('color: black; font-style: 10px')

    put_text('')

    put_row([put_image(map_original, width = '1000px'),
             put_column([put_text("Map Features").style('font-size: 30px'), 
             put_button("Toggle Map", onclick=lambda: toast("will change map type"), color='success', outline=True),
             put_button("Route Information", onclick=lambda: DisplayRouteInfo(StartingPoint, Destination), color='success', outline=True),
             put_button("Zoom In", onclick=lambda: ZoomIn(StartingPoint, Destination), color='success', outline=True)])], size='85% 10px 15%')


    #put_image('https://www.railwayage.com/wp-content/uploads/2021/06/Amtrak-2035.jpg')
    

    #put_markdown(r""" # Map Features
#""")

    #put_column([put_button("Toggle Map", onclick=lambda: toast("will change map type"), color='success', outline=True),
    #         put_button("Route Information", onclick=lambda: DisplayRouteInfo(StartingPoint, Destination), color='success', outline=True),
     #        put_button("Zoom In", onclick=lambda: ZoomIn(StartingPoint, Destination), color='success', outline=True)])




def DisplayRouteInfo(StartingPoint, Destination):

    #popup('Route information', 'Information')

    #Starting in Boston
    if StartingPoint == 'Boston':

        if Destination == 'Washington DC':
            popup('Route Information', 'Your train will begin in ' + StartingPoint + ' and will travel through Rhode Island, Connecticut, New York, New Jersey, Deleware, and Maryland on the route to ' + Destination  )

        if Destination == 'New York City':
            popup('Route Information', 'Your train will begin in ' + StartingPoint + ' and will travel through Rhode Island, and Connecticut on the route to ' + Destination  )
    
            
            
    else:
        popup('Route Information', 'Here is the information for a route from ' + StartingPoint + ' to ' + Destination + '.')

    #Boston: 'Your train will begin in ' + StartingPoint + ' and will travel through Rhode Island, Connecticut, New York, 
    #New Jersey, Deleware, and Maryland on the route to ' Destination 


def ZoomIn(StartingPoint, Destination):

    clear()

    img = open('RailTrac.png', 'rb').read() 

    put_row([put_image(img, width='100px'),put_markdown(r""" # RailTrac Route Display
""")], size='35% 65%')


    put_row([put_button("Home", onclick=lambda: showMenu(), color='success', outline=True),
             put_button("Logout", onclick=lambda: loginPage(), color='success', outline=True),
             put_button("Change Locations", onclick=lambda: Selection(), color='success', outline=True)])

    
    userDB = UserDBM('userDB.txt')
    db = trackDB.TrackDB()
    db.initialize();
    
    path = db.shortestPath([StartingPoint, Destination])
    userDB.writeUserHistory(StartingPoint, Destination, path.eta)

    put_text('')

    put_row([put_text(''),
             put_text(StartingPoint + " to " + Destination).style('font-size: 35px')], size='25% 75%')



    put_text('')

    put_row([put_text(''),
             put_text("ETA is", path.eta, "hours").style('color: red; font-size: 20px')], size='35% 65%')


    #Some text informing the user that their route is being displayed

    s = ''
    for i in range(len(path.route)-1):
        s += path.route[i] + ', '
    s += path.route[len(path.route)-1]

    put_text("The route from " + StartingPoint + " to " + Destination + " is: " + s).style('color: black; font-style: 10px')

    put_text('')


    put_text('')

    #image of west coast
    #put_image('https://www.up.com/cs/groups/public/@uprr/@corprel/documents/digitalmedia/omhq17a129812003487.gif')


    #If Starting point is BOSTON
    if StartingPoint == 'Boston':
       if Destination == 'Washington DC':
        put_image('https://www.amtrak.com/content/dam/projects/dotcom/english/public/images/nec/northeast-corridor-map.jpg/_jcr_content/renditions/original')
        
       if Destination == 'Chicago':
         put_image('https://upload.wikimedia.org/wikipedia/commons/1/1d/Amtrak_Lake_Shore_Limited.svg')

       if Destination == 'New York City':
        put_image('https://www.amtrak.com/content/dam/projects/dotcom/english/public/images/nec/northeast-corridor-map.jpg/_jcr_content/renditions/original')


        #If Starting point is WASHINGTON DC
    if StartingPoint == 'Washington DC':
       if Destination == 'Boston':
        put_image('https://www.amtrak.com/content/dam/projects/dotcom/english/public/images/nec/northeast-corridor-map.jpg/_jcr_content/renditions/original')

       if Destination == 'New York City':
        put_image('https://www.amtrak.com/content/dam/projects/dotcom/english/public/images/nec/northeast-corridor-map.jpg/_jcr_content/renditions/original')

       if Destination == 'Chicago':
            put_image('https://upload.wikimedia.org/wikipedia/commons/0/04/Amtrak_Capitol_Limited.png')


        #If Starting point is CHICAGO
    if StartingPoint == 'Chicago':
        if Destination == 'New York City':
         put_image('https://upload.wikimedia.org/wikipedia/commons/1/1d/Amtrak_Lake_Shore_Limited.svg')
         
        if Destination == 'Boston':
          put_image('https://upload.wikimedia.org/wikipedia/commons/1/1d/Amtrak_Lake_Shore_Limited.svg')

        if Destination == 'Washington DC':
            put_image('https://upload.wikimedia.org/wikipedia/commons/0/04/Amtrak_Capitol_Limited.png')


    #If Starting point is NEW YORK CITY
    if StartingPoint == 'New York City':
        if Destination == 'Chicago':
          put_image('https://upload.wikimedia.org/wikipedia/commons/1/1d/Amtrak_Lake_Shore_Limited.svg')

        if Destination == 'Boston':
          put_image('https://www.amtrak.com/content/dam/projects/dotcom/english/public/images/nec/northeast-corridor-map.jpg/_jcr_content/renditions/original')

        if Destination == 'Washington DC':
          put_image('https://www.amtrak.com/content/dam/projects/dotcom/english/public/images/nec/northeast-corridor-map.jpg/_jcr_content/renditions/original')

         



    put_markdown(r""" # Map Features
""")

    put_row([put_button("Toggle Map", onclick=lambda: toast("will change map type"), color='success', outline=True),
             put_button("Route Information", onclick=lambda: DisplayRouteInfo(StartingPoint, Destination), color='success', outline=True),
             put_button("Zoom Out", onclick=lambda: TrackGUI(StartingPoint, Destination), color='success', outline=True)])

    return()


    

# Start the RailTrac application
# start_server([Selection], port=80, debug=True, remote_access=True)