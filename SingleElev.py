from Building import *


class SingleElev:
<<<<<<< HEAD
    # myUpCalls = []
    # myDownCalls = []
    # jsonFile = 'C:\\Users\\roeyf\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Buildings\\B1.json'
    # csvFile = 'C:\\Users\\roeyf\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Calls\\Calls_a.csv'
    # myBuiding = Building(jsonFile, csvFile)
    # temp = myBuiding.myCalls[0]
    # print(temp)


    def elevDir(call):
        #This function will check in which direcdion the call is True for UP False for Down
        if call.srcFloor < call.destFloor:
            return True
        else:
            return  False

=======
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
>>>>>>> cee05586b7da829e842792d14687697ef2ee7e55
