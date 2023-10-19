from utils.helpers import readJSON, writeJSON
from utils.hash import hash_password
class User:
    __accessList = {
        1:["personal details"],
        2:["personal details", "sickness details", "drug prescriptions",  "lab test prescriptions"],
        3:["personal details",  "lab test prescriptions"],
        4:["personal details", "sickness details", "drug prescriptions",  "lab test prescriptions"],
    }

    def __init__(self, user_name, role):
        self.__user_name = user_name
        self.__role = role
    
    def getRole(self):
        return self.__role

    def work(self):
        pass

    def getuser_name(self):
        return self.__user_name

    def printDetailsofPatient(self, user_name):
        past_patients = readJSON("PatientData.json")
        if user_name in past_patients:
            pastient_data = past_patients[user_name]
            for key in self.__accessList[self.__role]:
                if key in pastient_data:
                    print(f"{key}: {pastient_data[key]}")
        else:
            print("Patient does not exist")
    

    def changePassword(self, user_name):
        pastUsers = readJSON("UserData.json")
        if user_name in pastUsers:
            password = input("New password: ").strip()
            pastUsers[user_name]['password'] = hash_password(password)
            writeJSON("UserData.json", pastUsers)
        else:
            print("User does not exist")