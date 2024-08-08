#Miras yapıları

class Databases():
    def __init__(self):
        self.DatabaseName = ""
        self.DatabaseIdentify = 0
        self.DatabaseUser = ""

class DatabaseUsers(Databases):
    def __init__(self):
        self.Username = ""
        self.Userpass = ""

DatabaseNumber1 = DatabaseUsers()
DatabaseNumber1.DatabaseName = "Master1"
DatabaseNumber1.DatabaseUser = "root"
DatabaseNumber1.DatabaseIdentify = 1
DatabaseNumber1.Username = "Michael"
DatabaseNumber1.Userpass = "11234"

