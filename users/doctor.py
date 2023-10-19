

from users.user import User
from utils.helpers import readJSON, writeJSON, getTimestamp



class Doctor(User):

    def __init__(self, username):
        super().__init__(username, 2)

    def addSicknessDetails(self, username):
        pastPatients = readJSON("PatientData.json")
        if username in pastPatients:
            sickness = input("Sickness details: ").strip()
            pastPatients[username]["Sickness details"].append(
                [sickness, getTimestamp()])
            writeJSON("PatientData.json", pastPatients)
        else:
            print("Patient does not exist")

    def addDrugPrescriptions(self, username):
        pastPatients = readJSON("PatientData.json")
        if username in pastPatients:
            sickness = input("Drug prescriptions: ").strip()
            pastPatients[username]["drug prescriptions"].append(
                [sickness, getTimestamp()])
            writeJSON("PatientData.json", pastPatients)
        else:
            print("Patient does not exist")

    def addLabTestPrescriptions(self, username):
        pastPatients = readJSON("PatientData.json")
        if username in pastPatients:
            sickness = input("Lab test prescriptions: ").strip()
            pastPatients[username]["lab test prescriptions"].append(
                [sickness, getTimestamp()])
            writeJSON("PatientData.json", pastPatients)
        else:
            print("Patient does not exist")

    def work(self):
        print("\nDoctor working...")
        print('''Enter 0 for viewing patient details.\nEnter 1 for adding sickness details.\nEnter 2 for adding drug prescriptions.\nEnter 3 for adding lab test prescriptions.\n\nEnter 9 for changing the password.''')
        choice = int(input("Your choice: ").strip())
        patientID = input("Patient email: ").strip()
        match choice:
            case 1:
                self.addSicknessDetails(patientID)
            case 2:
                self.addDrugPrescriptions(patientID)
            case 3:
                self.addLabTestPrescriptions(patientID)
            case 0:
                super().printDetailsOfPatient(patientID)
            case 9:
                super().changePassword()
            case _:
                print("Invalid Input")
