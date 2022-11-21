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
                    userHistory.departureLocation = currentLine[-3]
                    userHistory.arrivalLocation = currentLine[-2]
            return userHistory

    def newUser(self, username, password):
        with open(self.filename, 'r') as filestream:
            for line in filestream:
                currentLine = line.split(",")
                if (username == currentLine[0]):
                    return 'Error: User already exists'
        with open(self.filename, 'a') as filestream:
            filestream.write('\n')
            filestream.write(username)
            filestream.write(",")
            filestream.write(password)
        return 'New user successfully created!'

    def writeUserHistory(self, user, history):
        with open(self.filename, 'a+') as filestream:
            filestream.seek(0)
            for line in filestream:
                currentLine = line.split(",")
                if (user == currentLine[0]):
                    filestream.write(history[-2])
                    filestream.write(",")
                    filestream.write(history[-1])
                    filestream.write(",")
                    return


class UserHistory(object):
    def __init__(self, username):
        self.username = username
        self.departureLocation = ''
        self.arrivalLocation = ''
