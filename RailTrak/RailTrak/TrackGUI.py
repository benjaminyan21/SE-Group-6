from pywebio import *
from pywebio.output import *
from pywebio.input import *
from pywebio.output import put_text
from UserDBM import UserDBM
from pywebio import start_server
from lloginPage import *
import TrackDatabase as trackDB
from Path import Path
from AdminPage import *

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




def TrackGUI(StartingPoint, Destination):

    clear()

    img = open('Route_Display.png', 'rb').read()
    map_original = open('zoom_out(PNW).png', 'rb').read()


    put_row([put_image(img, width='1000px')])

    put_text('')

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
             put_button("Toggle Map", onclick=lambda: ToggleMap(StartingPoint, Destination), color='success', outline=True),
             put_button("Route Information", onclick=lambda: DisplayRouteInfo(StartingPoint, Destination), color='success', outline=True),
             put_button("Zoom In", onclick=lambda: ZoomIn(StartingPoint, Destination), color='success', outline=True)])], size='85% 10px 15%')
    
    put_markdown(r""" # Request Alternate Mode of Transportation
    """)
    put_link('Alternate Mode', app='altMode')

    put_markdown(r""" # Admin Page
    """)
    put_link('Make changes (Admin Only)', app='adminPage')

def ToggleMap(StartingPoint, Destination):

    clear()

    img = open('Route_Display.png', 'rb').read()
    ToggledMap = open('toggle_map.png', 'rb').read()

    put_row([put_image(img, width='1000px')])

    put_text('')


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

    put_row([put_image(ToggledMap, width = '1000px'),
             put_column([put_text("Map Features").style('font-size: 30px'), 
             put_button("Toggle Map", onclick=lambda: TrackGUI(StartingPoint, Destination), color='success', outline=True),
             put_button("Route Information", onclick=lambda: DisplayRouteInfo(StartingPoint, Destination), color='success', outline=True),
             put_button("Zoom In", onclick=lambda: ZoomIn(StartingPoint, Destination), color='success', outline=True)])], size='85% 10px 15%')

    put_markdown(r""" # Request Alternate Mode of Transportation
    """)
    put_link('Alternate Mode', app='altMode')

    put_markdown(r""" # Admin Page
    """)
    put_link('Make changes (Admin Only)', app='adminPage')



def ToggleZoomIn(StartingPoint, Destination):

    clear()

    img = open('Route_Display.png', 'rb').read() 

    put_row([put_image(img, width='1000px')])


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


    s = ''
    for i in range(len(path.route)-1):
        s += path.route[i] + ', '
    s += path.route[len(path.route)-1]

    put_text("The route from " + StartingPoint + " to " + Destination + " is: " + s).style('color: black; font-style: 10px')
    put_text('')
    put_text('')


    #If Starting point is BOSTON
    if StartingPoint == 'Boston':
       if Destination == 'Washington DC':
         zoom_toggle_map = open('TC-Boston_DC.png', 'rb').read()
        
       if Destination == 'Chicago':
         zoom_toggle_map = open('TC_Chicago_Boston.png', 'rb').read() 

       if Destination == 'New York City':
         zoom_toggle_map = open('TC-Boston_NY.png', 'rb').read() 


        #If Starting point is WASHINGTON DC
    if StartingPoint == 'Washington DC':
       if Destination == 'Boston':
         zoom_toggle_map = open('TC-Boston_DC.png', 'rb').read() 

       if Destination == 'New York City':
        zoom_toggle_map = open('TC-DC_NYC.png', 'rb').read() 

       if Destination == 'Chicago':
         zoom_toggle_map = open('TC_DC_Chicago.png', 'rb').read() 


        #If Starting point is CHICAGO
    if StartingPoint == 'Chicago':
        if Destination == 'New York City':
         zoom_toggle_map = open('TC_Chicago_NY.png', 'rb').read() 
         
        if Destination == 'Boston':
          zoom_toggle_map = open('TC_Chicago_Boston.png', 'rb').read() 

        if Destination == 'Washington DC':
          zoom_toggle_map = open('TC_DC_Chicago.png', 'rb').read() 


    #If Starting point is NEW YORK CITY
    if StartingPoint == 'New York City':
        if Destination == 'Chicago':
          zoom_toggle_map = open('TC_Chicago_NY.png', 'rb').read() 

        if Destination == 'Boston':
           zoom_toggle_map = open('TC-Boston_NY.png', 'rb').read() 

        if Destination == 'Washington DC':
           zoom_toggle_map = open('TC-DC_NYC.png', 'rb').read() 

         


    put_row([put_image(zoom_toggle_map, width = '1000px'),
         put_column([put_text("Map Features").style('font-size: 30px'), 
         put_button("Route Information", onclick=lambda: DisplayRouteInfo(StartingPoint, Destination), color='success', outline=True),
         put_button("Toggle Map", onclick=lambda: ZoomIn(StartingPoint, Destination), color='success', outline=True),
         put_button("Zoom Out", onclick=lambda: TrackGUI(StartingPoint, Destination), color='success', outline=True)])], size='85% 10px 15%')

    put_markdown(r""" # Request Alternate Mode of Transportation
        """)
    put_link('Alternate Mode', app='altMode')

    put_markdown(r""" # Admin Page
        """)
    
    put_link('Make changes (Admin Only)', app='adminPage')




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

    img = open('Route_Display.png', 'rb').read() 

    put_row([put_image(img, width='1000px')])


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
         zoom_map = open('Boston_DC.png', 'rb').read()
        
       if Destination == 'Chicago':
         zoom_map = open('Boston_Chicago.png', 'rb').read() 

       if Destination == 'New York City':
         zoom_map = open('Boston_NewYork.png', 'rb').read() 


        #If Starting point is WASHINGTON DC
    if StartingPoint == 'Washington DC':
       if Destination == 'Boston':
         zoom_map = open('Boston_DC.png', 'rb').read() 

       if Destination == 'New York City':
        zoom_map = open('NY-WDC.jpg', 'rb').read() 

       if Destination == 'Chicago':
         zoom_map = open('Chicago_DC.png', 'rb').read() 


        #If Starting point is CHICAGO
    if StartingPoint == 'Chicago':
        if Destination == 'New York City':
         zoom_map = open('Chicago_NewYork.png', 'rb').read() 
         
        if Destination == 'Boston':
          zoom_map = open('Boston_Chicago.png', 'rb').read() 

        if Destination == 'Washington DC':
          zoom_map = open('Chicago_DC.png', 'rb').read() 


    #If Starting point is NEW YORK CITY
    if StartingPoint == 'New York City':
        if Destination == 'Chicago':
           zoom_map = open('Chicago_NewYork.png', 'rb').read() 

        if Destination == 'Boston':
          zoom_map = open('Boston_NewYork.png', 'rb').read() 

        if Destination == 'Washington DC':
          zoom_map = open('NY-WDC.jpg', 'rb').read() 

         


    put_row([put_image(zoom_map, width = '1000px'),
             put_column([put_text("Map Features").style('font-size: 30px'), 
             put_button("Route Information", onclick=lambda: DisplayRouteInfo(StartingPoint, Destination), color='success', outline=True),
             put_button("Toggle Map", onclick=lambda: ToggleZoomIn(StartingPoint, Destination), color='success', outline=True),
             put_button("Zoom Out", onclick=lambda: TrackGUI(StartingPoint, Destination), color='success', outline=True)])], size='85% 10px 15%')


    put_markdown(r""" # Request Alternate Mode of Transportation
    """)
    put_link('Alternate Mode', app='altMode')

    put_markdown(r""" # Admin Page
     """)

    put_link('Make changes (Admin Only)', app='adminPage')

    return()


    

# Start the RailTrac application
# start_server([Selection], port=80, debug=True, remote_access=True)

