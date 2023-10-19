from users.admin import Admin 
from utils.helpers import readJSON, writeJSON
from utils.hash import hash_password
from users.doctor import Doctor
from users.patient import Patient
from users.receptionist import Receptionist

class Authentication:
    currentUser = None

    def login(self ):
        user_name = input("Username: ").strip()
        password = input("Password: ").strip()
        past_users = readJSON("UserData.json")
        if user_name in past_users:
            if past_users[user_name]['password'] == hash_password(password):
                role = past_users[user_name]['role']
                match role:
                    case 1:
                        self.currentUser = Admin(user_name)
                        return self.currentUser
                    case 2:
                        self.currentUser = Doctor(user_name)
                        return self.currentUser
                    case 3:
                        self.currentUser = Receptionist(user_name)
                        return self.currentUser
                    case 4:
                        self.currentUser = Patient(user_name)
                        return self.currentUser
                    case _:
                        print("Invalid role")
            else:
                print("Invalid password")
        else:
            print("Invalid username")
        return None