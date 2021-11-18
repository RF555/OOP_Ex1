import json
import csv
# import SingleElev
from Elevator import *
from Building import *
from myFunction import *
import pandas as pd

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # building1 = Building('C:\\Users\\Matanel\\PycharmProjects\\OOP_2021-main\\OOP_2021-main\\Assignments\\Ex1-Git\\data\\Ex1_input\\Ex1_Buildings\\B5.json')
    jsonFile = 'C:\\Users\\Matanel\\Desktop\\Ex1\\Ex1-Git\\data\\Ex1_input\\Ex1_Buildings\\B2.json'
    csvFile = 'C:\\Users\\Matanel\\Desktop\\Ex1\\Ex1-Git\\data\\Ex1_input\\Ex1_Calls\\Calls_a.csv'
    #jsonFile = 'C:\\Users\\Roey\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Buildings\\B1.json'
    #csvFile = 'C:\\Users\\Roey\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Calls\\Calls_a.csv'
    # jsonFile = 'C:\\Users\\roeyf\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Buildings\\B1.json'
    # csvFile = 'C:\\Users\\roeyf\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Calls\\Calls_a.csv'
    building1 = Building(jsonFile, csvFile)
    allCalls = building1.myCalls
    upcalls = building1.up_calls
    downcalls = building1.down_calls
    if len(building1.myElevators) == 1:
        for call in building1.myCalls:
            myFunction.allocateElev(allCalls , building1.myElevators[0],call)
        for call in building1.myCalls:
            print(call)
    else:
        for call in building1.myCalls:
            if call.allocatedElev != -1:
                continue
            else:
                for elev in building1.myElevators:
                    #LEVEL!
                    if elev.flag == 0:
                        myFunction.change_flag(elev, call)
                        myFunction.allocateElev(allCalls, elev, call)
                        myFunction.elevatorTimeline(elev, call)
                        if elev.flag == 1:
                            myFunction.update_up_down_call(elev,call,building1.up_calls)
                        elif elev.flag ==-1:
                            myFunction.update_up_down_call(elev,call,building1.down_calls)
                        #UP
                        if elev.flag == 1:
                            for up_call in upcalls:
                                if up_call.allocatedElev != -1:
                                    continue
                                else:
                                    if myFunction.pickUpOption(elev, up_call):
                                        up_call.allocatedElev = 0
                                        myFunction.allocateElev(allCalls, elev, up_call)
                                        myFunction.change_flag(elev, up_call)
                                        myFunction.elevatorTimeline(elev, up_call)
                        #DOWN
                        else:
                            for down_call in downcalls:
                                if down_call.allocatedElev != -1:
                                    continue
                                else:
                                    if myFunction.pickUpOption(elev, down_call):
                                        down_call.allocatedElev = 0
                                        myFunction.allocateElev(allCalls, elev, down_call)
                                        myFunction.change_flag(elev, down_call)
                                        myFunction.elevatorTimeline(elev, down_call)
                    #elevetor not LEVEL
                    else:
                        #UP
                        if call.call_dir:
                            if float(call.request_time) > float(elev.timeLine[-1]):
                                elev.flag =0
                                for cell in range(len(elev.timeLine)):
                                    elev.timeLine[cell] = 0
                            else:
                             continue
                        #DOWN
                        else:
                            if float(call.request_time) > float(elev.timeLine[0]):
                                elev.flag =0
                                for cell in range(len(elev.timeLine)):
                                    elev.timeLine[cell] = 0
                            else:
                                continue
        for call in building1.myCalls:
            print(call)
    counter =0
    for call in building1.myCalls:
        if call.allocatedElev == -1:
            counter = counter +1
    #myFunction.fromArrayToCsv(building1.myCalls)
    with open('output.csv','w') as myfile:
        for l in building1.myCalls:
            myfile.write(l.__str__())
            myfile.write('\n')
    print(counter)
##################################################################################################################################################################

    # Here are the test for my functions
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
    #myFunction.elevatorTimeline(building1.myElevators[0] , temp)
    #print(building1.myElevators[0].timeLine)
    #newCall = Call(11,1,7,0,0,-1)
    #newCall1 = Call(12, 1, 7, 0, 0, -1)
    #print(myFunction.pickUpOption(building1.myElevators[0],newCall))
    #print(myFunction.pickUpOption(building1.myElevators[0], newCall1))
    #myFunction.elevatorTimeline(building1.myElevators[0], temp1)
    #print(building1.myElevators[0].timeLine)
    # print(building1.myCalls[1])
    # #print(building1.myCalls[1].allocatedElev)
    # if float(temp.request_time) > myFunction.time_to_src(building1.myElevators[0] , temp):
    #      myFunction.allocateElev(building1.myCalls, building1.myElevators[0], temp)
    # print(building1.myElevators[0].myCalls)
    # myFunction.elevatorTimelineUp(building1.myElevators[0], temp)
    # print(building1.myElevators[0].timeLine)
    # print(myFunction.pickUpOption(building1.myElevators[0],temp1))
    # myFunction.allocateElev(building1.myCalls, building1.myElevators[0], temp1)
    # building1.myElevators[0].flag = -1
    # building1.myElevators[0].curr_floor = myFunction.update_curr_floor(building1.myElevators[0], temp1)
    # myFunction.elevatorTimelineUp(building1.myElevators[0],temp1)
    # print(building1.myElevators[0].timeLine)
    #newlist = [1,2,3,4,5,6,7,8,9]
    #print(newlist)
    #newlist.sort(reverse=True)
    #print(newlist)
    #print(building1.myCalls[1])
    #print(building1.myCalls[1].allocatedElev)
    #myFunction.elevatorTimelineUp(building1.myElevators[0], temp1)
    #print(building1.myElevators[0].timeLine)
    # for call in building1.up_calls:
    # print(call)
###############################################################################################################################################################

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
