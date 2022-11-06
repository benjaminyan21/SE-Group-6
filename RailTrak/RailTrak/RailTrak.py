from pywebio import *
from pywebio.output import *
from pywebio.input import *

def main():
    pass 
from pywebio.output import *
from pywebio.input import *

def main():
    '''
    An interactive web app that displays Admin main page
    '''

    #desktop = os.path.expanduser("~/Desktop")
    #shutil.copy(logo.png, desktop)

    #img = open(os.path.expanduser("~/Desktop"), 'rb').read()
    #put_image('/desktop/logo.jpg', width='50px')

    #img = open('/mnt/app/logo.jpg', 'rb').read()  
    put_image('https://i.imgur.com/y682Iqt.jpg', width='150px')

    #put_image('https://www.python.org/static/img/python-logo.png')

    put_markdown('# Hello Admin')
    put_text('Map')

    put_image('https://understandingsocietyglobaledition.files.wordpress.com/2011/08/photo-12.png')

    #put_markdown('## View Map, Add, Change, Remove')

    ##username = input('Input your name')
    ##put_text('Hello, %s' % username)

    put_text(' ')
    put_grid([
    [put_button('View Map', onclick=lambda: toast("Set to View"), color='success', outline=True), 
    put_button('Add', onclick=lambda: toast("Set to Add"), color='success', outline=True), 
    put_button('Change', onclick=lambda: toast("Set to Change"), color='success', outline=True), 
    put_button('Delete', onclick=lambda: toast("Set to Delete"), color='success', outline=True)],
], cell_width='250px', cell_height='100px')
