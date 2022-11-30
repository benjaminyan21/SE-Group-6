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
    put_markdown(r""" # RailTrac Homepage
    """)
    put_link('Login', app='loginPage')
    put_text('')
    put_link('Sign-Up', app='newUserRegister')
    put_text('')
    
    img = open('RailTrac.png', 'rb').read()
    put_image(img, width='1000px')

# Start the RailTrac application
start_server([index, loginPage, newUserRegister, Selection, showHistoryLog, adminPage, altMode, forgotpassword], port=80, debug=True, remote_access=False)
