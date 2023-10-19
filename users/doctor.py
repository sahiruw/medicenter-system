

from users.user import User
from utils.helpers import readJSON, writeJSON, getTimestamp
from utils.hash import hash_password


class Doctor(User):

    def __init__(self, username):
        super().__init__(username, 2)

    def addSicknessDetails(self, username):
        pastPatients = readJSON("PatientData.json")
        if username in pastPatients:
            sickness = input("Enter sickness details: ").strip()
            pastPatients[username]["sickness details"].append(
                [sickness, getTimestamp()])
            writeJSON("PatientData.json", pastPatients)
        else:
            print("Patient does not exist")

    def addDrugPrescriptions(self, username):
        pastPatients = readJSON("PatientData.json")
        if username in pastPatients:
            sickness = input("Enter drug prescriptions: ").strip()
            pastPatients[username]["drug prescriptions"].append(
                [sickness, getTimestamp()])
            writeJSON("PatientData.json", pastPatients)
        else:
            print("Patient does not exist")

    def addLabTestPrescriptions(self, username):
        pastPatients = readJSON("PatientData.json")
        if username in pastPatients:
            sickness = input("Enter lab test prescriptions: ").strip()
            pastPatients[username]["lab test prescriptions"].append(
                [sickness, getTimestamp()])
            writeJSON("PatientData.json", pastPatients)
        else:
            print("Patient does not exist")

    def work(self):
        print("\nDoctor working...")
        print('''Print 0 to view patient details.\nPrint 1 to add sickness details.\nPrint 2 to add drug prescriptions.\nPrint 3 to add lab test prescriptions.\n\nPrint 9 to change password.''')
        choice = int(input("Enter your choice: ").strip())
        patientID = input("Enter patient email: ").strip()
        if choice == 1:
            self.addSicknessDetails(patientID)
        elif choice == 2:
            self.addDrugPrescriptions(patientID)
        elif choice == 3:
            self.addLabTestPrescriptions(patientID)
        elif choice == 0:
            super().printDetailsofPatient(patientID)
        elif choice == 9:
            super().changePassword()
        else:
            print("Invalid choice")
