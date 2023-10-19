

from users.user import User
from utils.helpers import readJSON, writeJSON
from utils.hash import hash_password,generate_random_password


class Receptionist(User) :

    def __init__(self, username):
        super().__init__( username, 3)

    def addPatient(self, username,pw):
        pastUsers = readJSON("UserData.json")
        if username in pastUsers:
            print("User already exists")
            return

        pastUsers[username] = {'role': 4, 'password': hash_password(pw)}
        writeJSON("UserData.json", pastUsers)
        
        name = input("Patient name: ").strip()
        age = input("Patient age: ").strip()
        contactNo = input("Patient contact number: ").strip()
    
        pastPatients = readJSON("PatientData.json")

        pastPatients[username] = {"personal details" : {'age': age, 'contactNo': contactNo, 'name': name},  
                                  "sickness details": [], "drug prescriptions": [],  "lab test prescriptions": []}
        print(pastPatients)
        writeJSON("PatientData.json", pastPatients)

    
    def work(self):
        print("\nReceptionist working...")
        print ('''Enter 0 for getting patient details.\nEnter 1 for registering a new patient.\nEnter 9 for changing password.''')
        choice = int(input("Enter your choice: ").strip())
        if choice == 1:
            username = input("Patient email: ").strip()
            pw = input("Password: ").strip()
            self.addPatient(username, pw)
        elif choice == 0:
            patientID = input("Patient email: ").strip()
            super().printDetailsofPatient(patientID)
        elif choice == 9:
            super().changePassword()
        else:
            print("Invalid Input")

