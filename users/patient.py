

from users.user import User
from utils.helpers import readJSON, writeJSON
from utils.hash import hash_password

class Patient(User) :

    def __init__(self, username):
        super().__init__( username, 4)


    
    def work(self):
        print("\nPatient working...")
        print ('''Print 0 to view patient details.\nPrint 9 to change password..''')
        choice = int(input("Enter your choice: ").strip())
        if choice == 1:
            pass
        elif choice == 0:
            patientID = input("Enter patient email: ").strip()
            super().printDetailsofPatient(patientID)
        elif choice == 9:
            super().changePassword()
        else:
            print("Invalid choice")

