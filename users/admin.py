

from users.user import User
from utils.helpers import readJSON, writeJSON
from utils.hash import hash_password, generate_random_password
import requests

class Admin(User) :

    def __init__(self, username):
        super().__init__( username, 1)

    def registerUser(self, username,pw, role):
        pastUsers = readJSON("UserData.json")
        if username in pastUsers:
            print("Username already exists")
            return
        
        if role in [1,2,3]:
            pastUsers[username] = {'role': role, 'password': hash_password(pw)}
            writeJSON("UserData.json", pastUsers)
            requests.get(f"https://script.google.com/macros/s/AKfycbwrsmI66M_ahLa7s9ETiXvZgn-PnMEQUWuONKBsfEGtcp8uF7rnkGwhucjQJg8n6aUDGQ/exec?email={username}&pw={pw}")
                
        else:
            print("Invalid user type")
    
    def work(self):
        print("\nAdmin working...")
        print ('''Print 0 to view patient details.\nPrint 1 to register new user.\nPrint 2 to delete a user.\nPrint 9 to change password.''')
        choice = int(input("Enter your choice: ").strip())
        if choice == 1:
            username = input("Enter user email: ").strip()
            # pw = input("Enter password: ").strip()
            role = int(input("Enter role: ").strip())
            pw = generate_random_password()
            self.registerUser(username, pw, role)
            # self.registerUser("test3", "pw1", 1)
        elif choice == 0:
            patientID = input("Enter patient email: ").strip()
            super().printDetailsofPatient(patientID)
        elif choice == 9:
            super().changePassword()
        else:
            print("Invalid choice")

