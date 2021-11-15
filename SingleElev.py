from Building import *


class SingleElev:
    # def __init__(self, UpCalls, DownCalls, elevid, speed, minfloor, maxfloor, closetime, opentime, starttime, stoptime):
    #     self.elevid = elevid
    #     self.speed = speed
    #     self.minFloor = minfloor
    #     self.maxFloor = maxfloor
    #     self.closeTime = closetime
    #     self.openTime = opentime
    #     self.startTime = starttime
    #     self.stopTime = stoptime
    #     self.UpCalls = UpCalls
    #     self.DownCalls = DownCalls

    jsonFile = 'C:\\Users\\roeyf\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Buildings\\B1.json'
    csvFile = 'C:\\Users\\roeyf\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Calls\\Calls_a.csv'
    myBuilding = Building(jsonFile, csvFile)
    allCalls = myBuilding.myCalls
    UpCalls = myBuilding.up_calls
    DownCalls = myBuilding.down_calls
    myDirCalls = []
    if allCalls[0].call_dir == True:
        myDirCalls = UpCalls
    else:
        myDirCalls = DownCalls
    myCalls = []
    up = allCalls[0].call_dir
    tempC = None
    for i in myDirCalls.__sizeof__():
        if i == myDirCalls[0]:
            myCalls.append(myDirCalls[0])
            tempC = myDirCalls[0]
        elif up & tempC.srcFloor < myDirCalls[i + 1].srcFloor:
            myCalls.append(myDirCalls[i])
            tempC = myDirCalls[i]
        elif (not up) & tempC.srcFloor > myDirCalls[i + 1].srcFloor:
            myCalls.append(myDirCalls[i])
            tempC = myDirCalls[i]
