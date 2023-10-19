import json
from datetime import datetime

def readJSON(filename):
    with open(filename, "r") as json_data_file:
        data = json.load(json_data_file)
    return data

def writeJSON(filename, data):
    with open(filename, "w") as json_data_file:
        json.dump(data, json_data_file)

def getTimestamp():
    now = datetime.now()
    return now.strftime("%A, %B %d, %Y %I:%M %p")
