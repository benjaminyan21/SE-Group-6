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

    #Trip information displayed
    put_markdown('# Trip 1 (Houston - Dallas)')
    put_text('Current Map Path')
    
    #This is an image taken directly from Google Maps, might change later.
    put_image('https://www.google.com/maps/vt/data=aVjKhmJfFHs-olDWKtwvXJmDtQa08SVqGfO6rT5duov92S7Gp3pYGDyZLWmB9LTPcnp32r66yp5J8Pdo7ruoYbPXRKEooUkAJWXliW6bQ72Tl7B-9MUin5_itHwLafk3r3oiAA-8vHyElS7Wo40UqSUaOYSM94obwP-U7mdMjopbXw,I5UyRqn7K6QjC0-4l4g8lnUevTIjMjGzXpM0ux6ROnm4w_opo4e9gmxRs_BQD2f60ikRtB_P1yqg5mFstMiz5WeRUNW-Y0wMthmTreMmBskifDhsXdPVrjunA5I038qifE2YQO0T6CoO7LAOwZ1cEc0h_VYCYyTkIbU92yyYKVValoPWIqOq27ZVcanPB1vunS4rgoh8CHojPdOGo88ldy7jHlW7WBOQeAC5irq5Ti8pqW9DDhHMhRSPXgZlSkWHbIGSciXZe3bdqwEYNdfhsI-6Vq41BsB6qC4tKu4V4Khl0U-KL60sBJsYdBvWZXsaJ8VIe0a4INd7v7DyqVfswFxLGqnVWuCfvrrhzuOm?scale=1&h=200&w=652', width='1000px')
    put_warning('CURRENT ETA: 3 hours')

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

 
