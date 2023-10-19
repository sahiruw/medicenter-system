from utils.helpers import readJSON, writeJSON
from utils.hash import hash_password
class User:
    __accessList = {
        1:["personal details"],
        2:["personal details", "sickness details", "drug prescriptions",  "lab test prescriptions"],
        3:["personal details",  "lab test prescriptions"],
        4:["personal details", "sickness details", "drug prescriptions",  "lab test prescriptions"],
    }

    def __init__(self, username, role):
        self.__username = username
        self.__role = role
    
    def getRole(self):
        return self.__role

    def work(self):
        pass

    def getusername(self):
        return self.__username

    def printDetailsofPatient(self):
        pastPatients = readJSON("PatientData.json")
        if self.__role == 4:
            username = self.__username
        else:
            username = input("Enter patient email: ").strip()
            
        if username in pastPatients:
            patientData = pastPatients[username]
            for key in self.__accessList[self.__role]:
                if key in patientData:
                    print(f"{key}: {patientData[key]}")
        else:
            print("Patient does not exist")
    

    def changePassword(self, username):
        pastUsers = readJSON("UserData.json")
        if username in pastUsers:
            password = input("Enter new password: ").strip()
            pastUsers[username]['password'] = hash_password(password)
            writeJSON("UserData.json", pastUsers)
        else:
            print("User does not exist")