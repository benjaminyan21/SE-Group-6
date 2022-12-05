from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from UserDBM import UserDBM
from TrackGUI import *
from history_log import showHistoryLog
from lloginPage import loginPage, newUserRegister
from AdminPage import adminPage
from alternativeMethodOfTransportation import altMode
from forgotpassword import forgotpassword

# Index / homepage of the RailTrac website
def index():
    clear()

    img = open('RailTrac_Homepage.png', 'rb').read() 
    put_row([put_image(img, width='1000px')])
    put_text('')

    put_row([put_button("Login", onclick=lambda: loginPage(), color='success', outline=True)], size= '100px')

    put_text('')

    put_row([put_button("Sign-Up", onclick=lambda: newUserRegister(), color='success', outline=True)], size='100% 100px')

    put_text('')

# Start the RailTrac application
start_server([index, loginPage, newUserRegister, Selection, showHistoryLog, adminPage, altMode, forgotpassword], port=80, debug=True, remote_access=False)
