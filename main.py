import json
from Elevator import *
from Building import *
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    building1 = Building('C:\\Users\\Matanel\\PycharmProjects\\OOP_2021-main\\OOP_2021-main\\Assignments\\Ex1-Git\\data\\Ex1_input\\Ex1_Buildings\\B5.json')
    print(building1.getminfloor())
    building1.minFloor = -65132468
    print(building1.getminfloor())
    print(building1.getmaxfloor())
    #print(building1.)
    #print(building1)
    #f = open('B2.json')
    #data = json.load(f)
    #elev = data["_elevators"]
    #print(elev[0]["_speed"])
    #print(elev[1])
    #elev1 = Elevator(elev[0]["_id"],elev[0]["_speed"],elev[0]["_minFloor"],elev[0]["_maxFloor"],elev[0]["_closeTime"],elev[0]["_openTime"],elev[0]["_startTime"],elev[0]["_stopTime"])
    # print(elev1)
    #elev1= Elevator(1,10,-10,100,1,1,1,1)
    #print(elev1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
