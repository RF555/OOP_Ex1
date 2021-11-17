import main
from Building import *
class myFunction:
    def elevDir(call):
        #This function will check in which direcdion the call is True for UP False for Down
        if call.srcFloor < call.destFloor:
            return True
        else:
            return  False

    def isElevDone(elevator):
        #This function check if the elevator finished her calls and ready for new one
        if len(elevator.myCalls) == 0:
            return True
        else:
            return False

    def addToCalls(elevator , call):
        tempCalls = elevator.myCalls
        if call.srcFloor not in tempCalls:
            elevator.myCalls.append(call.srcFloor)
        if call.destFloor not in tempCalls:
            elevator.myCalls.append(call.destFloor)

    def elevatorTimelineUp(elevetor , call):
        temp = len(elevetor.timeLine)
        if elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor] == 0:
            elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor] = float(call.request_time) + myFunction.time_to_src(elevetor,call)
            for cell in range(int(call.srcFloor) - elevetor.minFloor +1,temp):
                #if cell + elevetor.minFloor == call.srcFloor:
                    #continue
                floorDiff = cell - (int(call.srcFloor) - elevetor.minFloor)
                elevetor.timeLine[cell] = (elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor] + (floorDiff/elevetor.speed) + elevetor.closeTime + elevetor.startTime)
        else:
            for cell in range(int(call.srcFloor) - int(elevetor.minFloor), temp):
                elevetor.timeLine[cell] = elevetor.timeLine[cell] + (elevetor.openTime + elevetor.closeTime + elevetor.startTime + elevetor.stopTime)

    def elevatorTimelineDown(elevetor , call):
        temp = len(elevetor.timeLine)
        if elevetor.timeLine[call.srcFloor - elevetor.minFloor] == 0:
            elevetor.timeLine[call.srcFloor - elevetor.minFloor] = call.request_time
            for cell in range(elevetor.minFloor , call.srcFloor - elevetor.minFloor):
                print("hi")

    def allocateElev(callsList, elevetor, call):
        callTimeStemp = call.request_time
        allCalls = callsList
        for call in allCalls:
            if call.request_time == callTimeStemp:
                callIndex = callsList.index(call)
                newCall = Call(call.request_time, call.srcFloor, call.destFloor, call.elevStatus, call.elevIndex, elevetor.elevid)
                callsList.insert(callIndex,newCall)
                callsList.pop(callIndex+1)
                elevetor.myCalls.append(call.destFloor)
                elevetor.myCalls.append(call.srcFloor)
                elevetor.myCalls.sort()
                break

    def pickUpOptionup(elevetor , call):
            #we going up
            temp = int(call.srcFloor) - elevetor.minFloor
            if float(elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor]) > float(call.request_time):
                if call.srcFloor < elevetor.myCalls.pop():
                    return True
            return False

    def time_to_src(elevetor , call):
        src = int(call.srcFloor)
        if src == elevetor.curr_floor:
            return 0
        time = (abs(abs(elevetor.curr_floor) - abs(src)))/ elevetor.speed + elevetor.closeTime + elevetor.startTime
        return  time