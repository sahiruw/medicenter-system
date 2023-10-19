from users.admin import Admin 
from utils.helpers import readJSON, writeJSON
from utils.hash import hash_password
from users.doctor import Doctor
from users.patient import Patient
from users.receptionist import Receptionist

class Authentication:
    currentUser = None

    def login(self ):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        pastUsers = readJSON("UserData.json")
        if username in pastUsers:
            if pastUsers[username]['password'] == hash_password(password):
                role = pastUsers[username]['role']
                if role == 1:
                    self.currentUser = Admin(username)
                    return self.currentUser
                elif role == 2:
                    self.currentUser = Doctor(username)
                    return self.currentUser
                elif role == 3:
                    self.currentUser = Receptionist(username)
                    return self.currentUser
                elif role == 4:
                    self.currentUser = Patient(username)
                    return self.currentUser
                else:
                    print("Invalid role")
            else:
                print("Invalid password")
        else:
            print("Invalid username")
        return None