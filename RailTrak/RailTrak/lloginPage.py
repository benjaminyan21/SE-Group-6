#from pickle import TRUE
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from UserDBM import UserDBM
from forgotpassword import *

# This function gets the login from the user and validates it against the database
def loginPage(username=None, password=None):
    clear()
    if username is None:
        username, password = showLogin()
    
    userDB = UserDBM('userDB.txt')
    msg = userDB.validate(username, password)

    while (msg is not None):
        clear()
        put_error(msg)
        username, password = showLogin()
        msg = userDB.validate(username, password)

    f = open("currentUser.txt", "w")
    f.write(username)
    f.close()
    showMenu()

# Define the login function to show and receive input from user
def showLogin():
    put_row([put_button("Home", onclick=lambda: index(), color='success', outline=True)])
    put_markdown(r""" # RailTrac Login Page
    """)

    put_input('in1', label='Username')
    put_input('in2', label='Password', type='password')

    put_buttons(['Login'], lambda _: loginPage(pin.in1, pin.in2))
    put_link('Forgot Password?',app='forgotpassword')
    cont=True
    while cont:
        pin_wait_change('in1')
        pin_wait_change('in2')
    return pin.in1, pin.in2

# This function shows the main RailTrac menu from which the user can navigate to the history log
def showMenu():
    clear()

    img = open('RailTrac_Menu.png', 'rb').read()

    put_row([put_image(img, width='1000px')])

    put_text('')
    put_text('')


    put_link('Find a Route',app='Selection')
    put_text('')
    put_link('History Log',app='showHistoryLog')

# This functions allows for new users to register for the service
def newUserRegister():
    clear()
    put_row([put_button("Home", onclick=lambda: index(), color='success', outline=True)])

    put_markdown(r""" # New User Registration
    """)
    userDB = UserDBM('userDB.txt')

    userInfo = input_group("Enter new account information", [
        input('Username', name='username'),
        input('Password', name='pass', type=PASSWORD)])

    message = userDB.newUser(userInfo['username'], userInfo['pass'])
    put_text(message)

# This function logs out a user
def logoutPage():
    clear()
    f = open("currentUser.txt", "w")
    f.write('')
    f.close()
    put_success("You are now logged out")

    loginPage(None, None)

# Index / homepage of the RailTrac website
def index():
    clear()

    img = open('RailTrac_Homepage.png', 'rb').read() 

    put_row([put_image(img, width='1000px')])

    put_text('')

    put_row([put_button("Login", onclick=lambda: loginPage(), color='success', outline=True)], size='100% 100px')

    put_text('')

    put_row([put_button("New User Registration", onclick=lambda: newUserRegister(), color='success', outline=True)], size='100% 100px')

    put_text('')