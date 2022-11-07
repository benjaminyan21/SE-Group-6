from pywebio import *
from pywebio.output import *
from pywebio.input import *

def main():
    #An interactive web app that displays Admin main page

    '''
    This is logo for our project. I uploaded to imgur so that it would be easier
    to load it here from there.
    '''
    put_image('https://i.imgur.com/y682Iqt.jpg', width='150px')

    #Hello message for admin and label for the map.
    put_markdown('# Hello Admin')
    put_text('Map')

    '''
    This image comes from an online source. It is a picture of the US. I am using it as a placeholder
    for where our interactive map will go.
    '''
    put_image('https://understandingsocietyglobaledition.files.wordpress.com/2011/08/photo-12.png', width='1000px')

    '''
    The code for the 4 buttons a the bottom of the map. After a button is pressed, there is an 
    announcement at the top, telling the user which mode was activated. 
    '''
    put_text(' ')
    put_grid([
    [put_button('View Map', onclick=lambda: toast("Set to View"), color='success', outline=False), 
    put_button('Add', onclick=lambda: toast("Set to Add"), color='success', outline=True), 
    put_button('Change', onclick=lambda: toast("Set to Change"), color='success', outline=True), 
    put_button('Delete', onclick=lambda: toast("Set to Delete"), color='success', outline=True)],
], cell_width='250px', cell_height='100px')

