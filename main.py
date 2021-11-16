import json

#import SingleElev
from Elevator import *
from Building import *
from myFunction import *
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # building1 = Building('C:\\Users\\Matanel\\PycharmProjects\\OOP_2021-main\\OOP_2021-main\\Assignments\\Ex1-Git\\data\\Ex1_input\\Ex1_Buildings\\B5.json')
    # jsonFile = 'C:\\Users\\Matanel\\Desktop\\Ex1\\Ex1-Git\\data\\Ex1_input\\Ex1_Buildings\\B1.json'
    # csvFile = 'C:\\Users\\Matanel\\Desktop\\Ex1\\Ex1-Git\\data\\Ex1_input\\Ex1_Calls\\Calls_a.csv'
    jsonFile='C:\\Users\\Roey\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Buildings\\B1.json'
    csvFile='C:\\Users\\Roey\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Calls\\Calls_a.csv'
    building1 = Building(jsonFile, csvFile)
    temp = building1.myCalls[0]
    temp1 = building1.myCalls[1]
    print(building1.myCalls[1])
    print(building1.myCalls[1].allocatedElev)
    myFunction.allocateElev(building1.myCalls, building1.myElevators[0], temp1)
    print(building1.myCalls[1])
    print(building1.myCalls[1].allocatedElev)
    #Here are the test for my functions
    ####################################################################################
    # print(temp)
    # print(temp1)
    # print(myFunction.elevDir(temp))
    # print(myFunction.elevDir(temp1))
    # print(myFunction.isElevDone(building1.myElevators[0]))
    # print(building1.myElevators[0].myCalls)
    # building1.myElevators[0].flag = 0
    # print(myFunction.addToCalls(building1.myElevators[0], temp))
    # print(myFunction.addToCalls(building1.myElevators[0], temp))
    # print(building1.myElevators[0].myCalls)
    # myFunction.elevatorTimeline(building1.myElevators[0] , temp)
    # print(building1.myElevators[0].timeLine)
    # myFunction.elevatorTimeline(building1.myElevators[0], temp1)
    # print(building1.myElevators[0].timeLine)
    ######################################################################################
    # building1 = Building('B1.json')
    # print('original building1.getminfloor()=', building1.getminfloor())
    # building1.minFloor = -65132468
    # print('new value building1.getminfloor()=', building1.getminfloor())
    # print('original building1.getmaxfloor()=', building1.getmaxfloor())
    # print('\n\n\n')
    # print(building1.myCalls[0])
    # print(building1.)
    # print(building1)
    # f = open('B2.json')
    # data = json.load(f)
    # elev = data["_elevators"]
    # print(elev[0]["_speed"])
    # print(elev[1])
    # elev1 = Elevator(elev[0]["_id"],elev[0]["_speed"],elev[0]["_minFloor"],elev[0]["_maxFloor"],elev[0]["_closeTime"],elev[0]["_openTime"],elev[0]["_startTime"],elev[0]["_stopTime"])
    # print(elev1)
    # elev1= Elevator(1,10,-10,100,1,1,1,1)
    # print(elev1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
