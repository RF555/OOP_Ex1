import main
from Elevator import *
from Building import *


# class myFunction:
def elev_dir(call):
    # This function will check in which direcdion the call is True for UP False for Down
    if call.srcFloor < call.destFloor:
        return 1
    else:
        return -1


def is_elev_done(elevator):
    # This function check if the elevator finished her calls and ready for new one
    if len(elevator.myCalls) == 0:
        elevator.flag = 0
        return True
    else:
        return False


def add_to_calls(elevator, call):
    temp_calls = elevator.myCalls
    if call.srcFloor not in temp_calls:
        elevator.myCalls.append(call.srcFloor)
    if call.destFloor not in temp_calls:
        elevator.myCalls.append(call.destFloor)


def elevator_timeline(elevator, call):
    temp = len(elevator.timeLine)
    if elevator.flag == 1:
        if elevator.timeLine[int(call.srcFloor) - elevator.minFloor - 1] == 0:
            elevator.timeLine[int(call.srcFloor) - elevator.minFloor] = float(
                call.request_time) + time_to_src(elevator, call)
            for cell in range(int(call.srcFloor) - elevator.minFloor + 1, temp):
                # if cell + elevator.minFloor == call.srcFloor:
                # continue
                floor_diff = cell - (int(call.srcFloor) - elevator.minFloor)
                elevator.timeLine[cell] = (elevator.timeLine[int(call.srcFloor) - elevator.minFloor] + (
                        floor_diff / elevator.speed) + elevator.closeTime + elevator.startTime)
        else:
            for cell in range(int(call.srcFloor) - int(elevator.minFloor), temp):
                elevator.timeLine[cell] = elevator.timeLine[cell] + (
                        elevator.openTime + elevator.closeTime + elevator.startTime + elevator.stopTime)

    elif elevator.flag == -1:
        if elevator.timeLine[int(call.srcFloor) - elevator.minFloor - 1] == 0:
            elevator.timeLine[int(call.srcFloor) - elevator.minFloor] = float(
                call.request_time) + time_to_src(elevator, call)
            for cell in range((int(call.srcFloor) - elevator.minFloor) - 1, -1, -1):
                floor_diff = (int(call.srcFloor) - elevator.minFloor) - cell
                elevator.timeLine[cell] = (elevator.timeLine[int(call.srcFloor) - elevator.minFloor] + (
                        floor_diff / elevator.speed) + elevator.closeTime + elevator.startTime)
        else:
            for cell in range(int(call.srcFloor) - int(elevator.minFloor) - 1, 0, -1):
                elevator.timeLine[cell] = elevator.timeLine[cell] + (
                        elevator.openTime + elevator.closeTime + elevator.startTime + elevator.stopTime)


def allocate_elev(callsList, elevator, call):
    call_time_stamp = call.request_time
    all_calls = callsList
    for call in all_calls:
        if call.request_time == call_time_stamp:
            call_index = callsList.index(call)
            new_call = Call(call.request_time, call.srcFloor, call.destFloor, call.elevStatus, call.elevIndex,
                            elevator.elevid)
            callsList.insert(call_index, new_call)
            callsList.pop(call_index + 1)
            elevator.elevCalls.append(call.destFloor)
            elevator.elevCalls.append(call.srcFloor)
            if elevator.flag == 1:
                elevator.elevCalls.sort()

                break
            elif elevator.flag == -1:
                elevator.elevCalls.sort(reverse=True)


def pick_up_option(elevator, call):
    # we going up
    temp = int(call.srcFloor) - elevator.minFloor
    if elevator.flag == 1:
        if float(elevator.timeLine[int(call.srcFloor) - elevator.minFloor]) > float(call.request_time):
            if call.srcFloor < elevator.elevCalls[-1]:
                return True
        return False
    elif elevator.flag == 0:
        if float(elevator.timeLine[int(call.srcFloor) - elevator.minFloor]) > float(call.request_time):
            if call.srcFloor < elevator.elevCalls[0]:
                return True
            return False
    else:
        if time_to_src(elevator, call) > float(call.request_time):
            return True
        else:
            return False


def time_to_src(elevetor, call):
    src = int(call.srcFloor)
    if src == elevetor.curr_floor:
        return 0
    time = (abs(abs(elevetor.curr_floor) - abs(src))) / elevetor.speed + elevetor.closeTime + elevetor.startTime
    return time


def update_curr_floor(elevator, call):
    if elevator.flag == 1:
        for cell in range(len(elevator.timeLine)):
            if float(elevator.timeLine[cell]) > float(call.request_time):
                return cell - 1
    elif elevator.flag == -1:
        for cell in range(len(elevator.timeLine) - 1, 0, -1):
            if float(elevator.timeLine[cell]) > float(call.request_time):
                return cell + 1


def change_flag(elevator, call):
    if int(call.srcFloor) < int(call.destFloor):
        elevator.flag = 1
    else:
        elevator.flag = -1


def from_array_to_csv(callsList):
    filename = 'output.csv'
    all = []
    for i in callsList:
        all.append(i.__dict__.values())
    with open(filename, 'w', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(all)


def update_up_down_call(elevetor, call, calls):
    if elevetor.flag == 1:
        for upcall in calls:
            if upcall == call:
                upcall.allocatedElev = elevetor.elevid
    elif elevetor.flag == -1:
        for downcall in calls:
            if downcall == call:
                downcall.allocatedElev = elevetor.elevid
