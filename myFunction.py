import main
from Elevator import *
from Building import *


class myFunction:
    def elevDir(call):
        # This function will check in which direcdion the call is True for UP False for Down
        if call.srcFloor < call.destFloor:
            return 1
        else:
            return -1

    def isElevDone(elevator):
        # This function check if the elevator finished her calls and ready for new one
        if len(elevator.myCalls) == 0:
            elevator.flag = 0
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
        if elevetor.flag == 1:
            if elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor - 1] == 0:
                elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor] = float(
                    call.request_time) + myFunction.time_to_src(elevetor, call)
                for cell in range(int(call.srcFloor) - elevetor.minFloor + 1, temp):
                    # if cell + elevetor.minFloor == call.srcFloor:
                    # continue
                    floorDiff = cell - (int(call.srcFloor) - elevetor.minFloor)
                    elevetor.timeLine[cell] = (elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor] + (
                                floorDiff / elevetor.speed) + elevetor.closeTime + elevetor.startTime)
            else:
                for cell in range(int(call.srcFloor) - int(elevetor.minFloor), temp):
                    elevetor.timeLine[cell] = elevetor.timeLine[cell] + (
                                elevetor.openTime + elevetor.closeTime + elevetor.startTime + elevetor.stopTime)

        elif elevetor.flag == -1:
            if elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor - 1] == 0:
                elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor] = float(
                    call.request_time) + myFunction.time_to_src(elevetor, call)
                for cell in range((int(call.srcFloor) - elevetor.minFloor) - 1, -1, -1):
                    floorDiff = (int(call.srcFloor) - elevetor.minFloor) - cell
                    elevetor.timeLine[cell] = (elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor] + (
                                floorDiff / elevetor.speed) + elevetor.closeTime + elevetor.startTime)
            else:
                for cell in range(int(call.srcFloor) - int(elevetor.minFloor) - 1, 0, -1):
                    elevetor.timeLine[cell] = elevetor.timeLine[cell] + (
                                elevetor.openTime + elevetor.closeTime + elevetor.startTime + elevetor.stopTime)

    def allocateElev(callsList, elevetor, call):
        callTimeStemp = call.request_time
        allCalls = callsList
        for call in allCalls:
            if call.request_time == callTimeStemp:
                callIndex = callsList.index(call)
                newCall = Call(call.request_time, call.srcFloor, call.destFloor, call.elevStatus, call.elevIndex,
                               elevetor.elevid)
                callsList.insert(callIndex, newCall)
                callsList.pop(callIndex + 1)
                elevetor.elevCalls.append(call.destFloor)
                elevetor.elevCalls.append(call.srcFloor)
                if elevetor.flag == 1:
                    elevetor.elevCalls.sort()

                    break
                elif elevetor.flag == -1:
                    elevetor.elevCalls.sort(reverse=True)

    def pickUpOption(elevetor, call):
        # we going up
        temp = int(call.srcFloor) - elevetor.minFloor
        if elevetor.flag == 1:
            if float(elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor]) > float(call.request_time):
                if call.srcFloor < elevetor.elevCalls[-1]:
                    return True
            return False
        elif elevetor.flag == 0:
            if float(elevetor.timeLine[int(call.srcFloor) - elevetor.minFloor]) > float(call.request_time):
                if call.srcFloor < elevetor.elevCalls[0]:
                    return True
                return False
        else:
            if myFunction.time_to_src(elevetor, call) > float(call.request_time):
                return True
            else:
                return False

    def time_to_src(elevetor, call):
        src = int(call.srcFloor)
        if src == elevetor.curr_floor:
            return 0
        time = (abs(abs(elevetor.curr_floor) - abs(src))) / elevetor.speed + elevetor.closeTime + elevetor.startTime
        return time

    def update_curr_floor(elevetor, call):
        if elevetor.flag == 1:
            for cell in range(len(elevetor.timeLine)):
                if float(elevetor.timeLine[cell]) > float(call.request_time):
                    return cell - 1
        elif elevetor.flag == -1:
            for cell in range(len(elevetor.timeLine) - 1, 0, -1):
                if float(elevetor.timeLine[cell]) > float(call.request_time):
                    return cell + 1

    def change_flag(elevetor, call):
        if int(call.srcFloor) < int(call.destFloor):
            elevetor.flag = 1
        else:
            elevetor.flag = -1

    def fromArrayToCsv(callsList):
        filename = 'output.csv'
        all = []
        for i in callsList:
            all.append(i.__dict__.values())
        with open(filename, 'w', newline="") as file:
            csvWriter = csv.writer(file)
            csvWriter.writerows(all)

    def update_up_down_call(elevetor, call, calls):
        if elevetor.flag == 1:
            for upcall in calls:
                if upcall == call:
                    upcall.allocatedElev = elevetor.elevid
        elif elevetor.flag == -1:
            for downcall in calls:
                if downcall == call:
                    downcall.allocatedElev = elevetor.elevid
