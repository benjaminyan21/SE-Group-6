from pywebio import *
from pywebio.output import *
from pywebio.input import *

def main():
    #Page that will show after the user selects forgot password

    put_image('https://i.imgur.com/y682Iqt.jpg', width='150px')

    #For recovery
    put_markdown('# Password Recovery')
    #put_text('Enter email associated with account')
    
    put_text('Your password will be sent to the email associated with your account')
    input('Enter email associated with account', type=TEXT)

    

    #Two buttons to submit or leave the page. 

    put_text(' ')
    put_grid([
    [put_button('Exit', onclick=lambda: toast("Set to Exit"), color='success', outline=False), 
    put_button('Submit', onclick=lambda: toast("Set to Submit"), color='success', outline=True), 
    ],
], cell_width='750px', cell_height='100px')
