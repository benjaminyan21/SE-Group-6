#Railtrak is our web app and this site is designed to change the method of transportation
from pywebio import *
from pywebio.output import *
from pywebio.input import *
from pywebio.output import put_text
from UserDBM import UserDBM
from pywebio import start_server
from lloginPage import *

def altMode():
    
    #Railtrak logo
    put_image('https://i.imgur.com/y682Iqt.jpg', width='150px')
    put_button("Home", onclick=lambda: showMenu(), color='success', outline=True)

    #Trip information displayed
    put_markdown('# Trip 1 (New York - Washington D.C.)')
    put_text('Current Map Path')
    
    #Image from Google Maps
    put_image('https://www.google.com/maps/vt/data=esIMGP_yWZtvmq3BIs44D4zbZ28oinatzo9RNHR1vWTt9r2lXg9UbgsrIKUzatQU7-sfeSJuyK-P7rCdEpOgvTM-IVBLMkETxlNXpaQXfVKNZtqbFdLYoADgcyWr5XL5X4ss1XbUS3FsQvOZno1D-aKnKduTZtqjpwcps8_stXxWJw,3YXvFr64ik4PCGhED0vkQdOilkeV-GOj9M0zOIqpO7HA63fpLSw4Pv5nrECTEh9mOoGhjRCPeR8003G7tt-UJUvLxxm_GFCk4qDGy0nR-Vvfv91C8fGiCeCOFPPmgz2TDh7J6-Kq0D5_cID85xjCyC8gQcc0aGALqSGZtiYdzYgifWeaqLPF5vhZoqeWy92pPkfIogHSC9qY5A-2TbTkPkSbI0q7tV4SENKiuweN4zwJuE54LPO6jSnXIXwSxCAhVyikEfN-dWTZxq_uXWwrn23qGzW2vGhBELck424sI24WrpgbDz0tuvYFD0YXNE7h1bAH61rQsVaTNLmCyBvs7KUFluLQSZmEU_ksbfAbRFH8Lj7CNIumQ9VB?scale=1&h=200&w=652', width='1000px')
    put_warning('CURRENT ETA: 4 hours')

    #Dropbox of endpoint destination selections
    endpoint = select("Change mode of transportation", ['Semi-Trailer', 'Plane', 'Truck', 'Train', 'Cargo Van'])

    #Checkbox to confirm it will replace old mode of transportation.
    checkbox("Confirm", options=['I UNDERSTAND IT WILL REPLACE OLD MODE OF TRANSPORTATION'])

    
    if 'Train' in [endpoint]:
        put_markdown('# Updated Mode of Transportation: Train')

    if 'Semi-Trailer' in [endpoint]:
        put_markdown('# Updated Mode of Transportation: Semi-Trailer')
    
    if 'Plane' in [endpoint]:
        put_markdown('# Updated Mode of Transportation: Plane')
    
    if 'Truck' in [endpoint]:
        put_markdown('# Updated Mode of Transportation: Truck')
    
    if 'Cargo Van' in [endpoint]:
        put_markdown('# Updated Mode of Transportation: Cargo Van')

 
