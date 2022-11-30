from pywebio import *
from pywebio.output import *
from pywebio.input import *
from lloginPage import *

def forgotpassword():
    clear()
    #Page that will show after the user selects forgot password
    #commemnt
    put_image('https://i.imgur.com/y682Iqt.jpg', width='150px')

    #Text
    put_markdown('# Password Recovery')
    
    
    input('Enter username associated with account', type=TEXT)
    #Take username and search db
    

    #Two buttons to submit or leave the page. 

    put_text(' ')
    put_grid([
    [put_button("Exit", onclick=lambda: index(), color='success', outline=False), 
    put_button("Submit", onclick=lambda: forgotpassword(), color='success', outline=True),
    ], #NEEDS CHANGE to submit and search DB for username then give password
], cell_width='750px', cell_height='100px')
     
