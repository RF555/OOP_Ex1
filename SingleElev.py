from Building import *


class SingleElev:
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

