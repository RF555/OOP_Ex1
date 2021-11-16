from Call import Call
from Elevator import *
import json
import csv


class Building:
    myElevators = None
    myCalls = None

    def __init__(self, jFile, csvFile):
        self.myElevators = []
        try:
            f = open(jFile)
            data = json.load(f)
            self.minFloor = data['_minFloor']
            self.maxFloor = data['_maxFloor']
            elev = data["_elevators"]
            for elev in data['_elevators']:
                tempElev = Elevator(elev['_id'], elev['_speed'], elev['_minFloor'], elev['_maxFloor'],
                                    elev['_closeTime'], elev['_openTime'], elev['_startTime'], elev['_stopTime'])
                self.myElevators.append(tempElev)
            f.close()
        except FileNotFoundError:
            print("No such file, please check your files and location")
        calls_arr = []
        try:
            with open(csvFile, newline='') as file:
                reader = csv.reader(file)
                i = 0
                for row in reader:
                    calls_arr.append(Call(row[1], row[2], row[3], row[4], row[5], -1))
                    i += 1
            self.myCalls = calls_arr
        except FileNotFoundError:
            print("No such file, please check your files and location")
        self.up_calls = []
        self.down_calls = []
        for i in range(len(self.myCalls)):
            if (self.myCalls[i].call_dir == True):
                self.up_calls.append(self.myCalls[i])
            else:  # the Call is DOWN
                self.down_calls.append(self.myCalls[i])

    def getminfloor(self):
        return self.minFloor

    def getmaxfloor(self):
        return self.maxFloor

    def __str__(self):
        try:
            myString = 'min floor is: ' + str(self.minFloor) + '\nmax floor is :' + str(
                self.maxFloor) + '\n------------------------------------------\n'
            for elev in self.myElevators:
                tempString = elev.__str__() + '\n'
                myString = myString + tempString + '------------------------------------------\n'
            return myString
        except AttributeError:
            return 'Nothing to print'
