from Elevator import *
import json


class Building:
    def __init__(self, jFile):
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
