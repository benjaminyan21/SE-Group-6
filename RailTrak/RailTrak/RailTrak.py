from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from UserDBM import UserDBM
from TrackGUI import *
from history_log import showHistoryLog
from lloginPage import loginPage, newUserRegister

# Index / homepage of the RailTrac website
def index():
    put_markdown(r""" # RailTrac Homepage
    """)
    put_link('Returning User Login', app='loginPage')
    put_text('')
    put_link('New User Registration', app='newUserRegister')

# Start the RailTrac application
start_server([index, loginPage, newUserRegister, Selection, showHistoryLog], port=80, debug=True, remote_access=True)
