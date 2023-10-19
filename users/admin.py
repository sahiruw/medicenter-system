

from users.user import User
from utils.helpers import readJSON, writeJSON
from utils.hash import hash_password


class Admin(User) :

    def __init__(self, user_name):
        super().__init__( user_name, 1)

    def registerUser(self, user_name,password, role):
        past_users = readJSON("userData.json")
        if user_name in past_users:
            print("User already exists")
            return
        
        if role in [1,2,3]:
            past_users[user_name] = {'role': role, 'password': hash_password(password)}
            writeJSON("userData.json", past_users)
            
                
        else:
            print("Invalid user type")
    
    def work(self):
        print("\nAdmin working...")
        print ('''Enter 0 for viewing the patient details.\nEnter 1 for Registering a  new user.\nEnter 2 to remove a user.\nEnter 9 for changing the password.''')
        choice = int(input("Enter your choice: ").strip())
        if choice == 1:
            user_name = input("User email: ").strip()
            role = int(input("Role: ").strip())
            password = input("Password: ").strip()
            self.registerUser(user_name, password, role)
        elif choice == 0:
            patient_id = input("Patient email: ").strip()
            super().printDetailsofPatient(patient_id)
        elif choice == 9:
            super().changePassword()
        else:
            print("Invalid Input")

