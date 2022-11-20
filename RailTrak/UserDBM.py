from datetime import datetime

class UserDBM(object):
    def __init__(self, filename):
        self.filename = filename

    def validate(self, username, password):
        with open(self.filename, 'r') as filestream:
            for line in filestream:
                currentLine = line.split(",")
                if (username == currentLine[0] and password == currentLine[1].rstrip()):
                    return None
            return 'Username or password is incorrect'

    def readUserHistory(self, user):
        userHistory = UserHistory(user)
        with open(self.filename, 'r') as filestream:
            for line in filestream:
                currentLine = line.split(",")
                if currentLine[0] == user:
                    userHistory.departureLocation = currentLine[2]
                    date = datetime.strptime(currentLine[3], "%I:%M %p")
                    userHistory.departureTime = date.strftime("%I:%M %p")
                    userHistory.arrivalLocation = currentLine[4]
                    date = datetime.strptime(currentLine[5], "%I:%M %p")
                    userHistory.arrivalTime = date.strftime("%I:%M %p")
            return userHistory

class UserHistory(object):
    def __init__(self, username):
        self.username = username
        self.departureLocation = ''
        self.departureTime = ''
        self.arrivalLocation = ''
        self.arrivalTime = ''
