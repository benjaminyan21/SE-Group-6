from pickle import PUT
from pywebio import *
from pywebio.output import *
from pywebio.input import *
from pywebio.pin import*
from lloginPage import *
from UserDBM import UserDBM


def forgotpassword():
    username=0
    clear()
    #Page that will show after the user selects forgot password
    
    put_image('https://i.imgur.com/y682Iqt.jpg', width='150px')

    #Text
    put_markdown('# Password Recovery')
    
    
    put_input('username', label='Enter username')
    #Take username and search db

    #Two buttons to submit or leave the page. 

    put_text(' ')
    put_grid([
    [put_button("Exit", onclick=lambda: index(), color='success', outline=False),
    put_button("Confirm", onclick=lambda: showpass(), color='success', outline=False), #NEEDS CHANGE to submit and search DB for username then give password
],], cell_width='750px', cell_height='100px')

def showpass():
    clear()
    put_text('Your password is 123')
    put_button("Exit", onclick=lambda: index(), color='success', outline=False)
'''
def search(username):
    
    userDB = UserDBM('userDB.txt')
    
    found = userDB.findUser(username)
    if(found):
        if(username =='dan'):
            popup("Your password is qwe")
        if(username =='abc'):
            popup("Your password is 123")
        if(username =='aaa'):
            popup("Your password is bbb")
'''
def index():
    clear();
    put_markdown(r""" # RailTrac Homepage
    """)
    put_link('Returning User Login', app='loginPage')
    put_text('')
    put_link('New User Registration', app='newUserRegister')
    put_text('')
    
    img = open('RailTrac.png', 'rb').read()  
    put_image(img, width='1000px')
     
