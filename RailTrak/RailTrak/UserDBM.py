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
                    userHistory.departureLocation = currentLine[-4]
                    userHistory.arrivalLocation = currentLine[-3]
                    userHistory.eta = currentLine[-2]
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
            filestream.write(',None,None, 0.5,')
        return 'New user successfully created!'

    def writeUserHistory(self, startpoint, endpoint, eta):
        with open("currentUser.txt", "r") as f:
            user = f.read()
            f.close()
        with open(self.filename, 'a+') as filestream:
            filestream.seek(0)
            for line in filestream:
                currentLine = line.split(",")
                if (user == currentLine[0]):
                    filestream.write(startpoint)
                    filestream.write(",")
                    filestream.write(endpoint)
                    filestream.write(",")
                    filestream.write(str(eta))
                    filestream.write(",")
                    return


class UserHistory(object):
    def __init__(self, username):
        self.username = username
        self.departureLocation = ''
        self.arrivalLocation = ''
        self.eta = 0.0
