

from users.user import User
from utils.helpers import readJSON, writeJSON
from utils.hash import hash_password

class Patient(User) :

    def __init__(self, username):
        super().__init__( username, 4)


    
    def work(self):
        print("\nPatient working...")
        print ('''Enter 0 for viewing the patient details.\nenter 9 for changing the password..''')
        choice = int(input("Your choice: ").strip())
        if choice == 1:
            pass
        elif choice == 0:
            patientID = input("Patient email: ").strip()
            super().printDetailsofPatient(patientID)
        elif choice == 9:
            super().changePassword()
        else:
            print("Invalid Input")

