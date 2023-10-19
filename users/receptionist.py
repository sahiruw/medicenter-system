

from users.user import User
from utils.helpers import readJSON, writeJSON
from utils.hash import hash_password,generate_random_password
import requests

class Receptionist(User) :

    def __init__(self, username):
        super().__init__( username, 3)

    def addPatient(self, username,pw):
        pastUsers = readJSON("UserData.json")
        if username in pastUsers:
            print("Username already exists")
            return

        pastUsers[username] = {'role': 4, 'password': hash_password(pw)}
        writeJSON("UserData.json", pastUsers)
        requests.get(f"https://script.google.com/macros/s/AKfycbwrsmI66M_ahLa7s9ETiXvZgn-PnMEQUWuONKBsfEGtcp8uF7rnkGwhucjQJg8n6aUDGQ/exec?email={username}&pw={pw}")

        name = input("Enter patient name: ").strip()
        age = input("Enter patient age: ").strip()
        contactNo = input("Enter patient contact number: ").strip()
    
        pastPatients = readJSON("PatientData.json")

        pastPatients[username] = {"personal details" : {'age': age, 'contactNo': contactNo, 'name': name},  
                                  "sickness details": [], "drug prescriptions": [],  "lab test prescriptions": []}
        print(pastPatients)
        writeJSON("PatientData.json", pastPatients)

    
    def work(self):
        print("\nReceptionist working...")
        print ('''Print 0 to view patient details.\nPrint 1 to register new patient.\nPrint 9 to change password.''')
        choice = int(input("Enter your choice: ").strip())
        if choice == 1:
            username = input("Enter patient email: ").strip()
            pw = generate_random_password()
            self.addPatient(username, pw)
        elif choice == 0:
            patientID = input("Enter patient email: ").strip()
            super().printDetailsofPatient(patientID)
        elif choice == 9:
            super().changePassword()
        else:
            print("Invalid choice")

