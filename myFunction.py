import main
from Building import *


class myFunction:
    def elevDir(call):
        # This function will check in which direcdion the call is True for UP False for Down
        if call.srcFloor < call.destFloor:
            return True
        else:
            return False

    def isElevDone(elevator):
        # This function check if the elevator finished her calls and ready for new one
        if len(elevator.myCalls) == 0:
            return True
        else:
            return False

    def addToCalls(elevator, call):
        tempCalls = elevator.myCalls
        if call.srcFloor not in tempCalls:
            elevator.myCalls.append(call.srcFloor)
        if call.destFloor not in tempCalls:
            elevator.myCalls.append(call.destFloor)

    def elevatorTimeline(elevetor, call):
        temp = len(elevetor.timeLine)
        if elevetor.timeLine[0 - elevetor.minFloor] == 0:
            elevetor.timeLine[0 - elevetor.minFloor] = call.request_time
            for cell in range(1 - elevetor.minFloor, temp):
                elevetor.timeLine[cell] = (elevetor.timeLine[0 - elevetor.minFloor] + (
                            (cell + elevetor.minFloor) / elevetor.speed) + elevetor.closeTime + elevetor.startTime)
        else:
            for cell in range(int(call.srcFloor) - int(elevetor.minFloor), temp):
                elevetor.timeLine[cell] = elevetor.timeLine[cell] + (
                            elevetor.openTime + elevetor.closeTime + elevetor.startTime + elevetor.stopTime)

    def allocateElev(callsList, elevetor, call):
        callTimeStemp = call.request_time
        allCalls = callsList
        for call in allCalls:
            if call.request_time == callTimeStemp:
                callIndex = callsList.index(call)
                newCall = Call(call.request_time, call.srcFloor, call.destFloor, call.elevStatus, call.elevIndex, 0)
                print(elevetor.elevid)
                print(newCall)
                callsList.insert(callIndex, newCall)
                callsList.pop(callIndex + 1)
                break
