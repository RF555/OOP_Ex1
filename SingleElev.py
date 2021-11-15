from Building import *


class SinglgeElev:
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
    myUpCalls = []
    myDownCalls = []
    jsonFile = 'C:\\Users\\roeyf\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Buildings\\B1.json'
    csvFile = 'C:\\Users\\roeyf\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Calls\\Calls_a.csv'
    myBuiding = Building(jsonFile, csvFile)
    if myBuiding.myElevators.__sizeof__() == 1:
