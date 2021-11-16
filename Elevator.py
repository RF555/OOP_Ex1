from Call import *
from SCall import *
import numpy as np


class Elevator:
    flag: bool
    my_q = None

    def __init__(self, elevid, speed, minfloor, maxfloor, closetime, opentime, starttime, stoptime):
        self.elevid = elevid
        self.speed = speed
        self.minFloor = minfloor
        self.maxFloor = maxfloor
        self.closeTime = closetime
        self.openTime = opentime
        self.startTime = starttime
        self.stopTime = stoptime
        self.flag = None
        self.curr_floor = 0
        self.myCalls = []
        self.timeLine = np.zeros(maxfloor - minfloor)

    def update_flag(self, SCall):
        if SCall.floor > self.curr:
            self.flag = True  # UP
        else:
            self.flag = False  # DOWN

    def i_to_j_time(self, i, j):
        if type(i) == type(j) == SCall:
            if i.floor == j.floor:
                return
            else:
                return self.closeTime + self.startTime + abs(
                    i.floor - j.floor) / self.speed + self.stopTime + self.openTime
        else:  # type is int
            return self.closeTime + self.startTime + abs(i - j) / self.speed + self.stopTime + self.openTime

    def __str__(self):
        return 'This elevator id is:' + str(self.elevid) + '\nthe speed is:' + str(self.speed) + \
               '\nthe min floor is:' + str(self.minFloor) + '\nthe max floor is:' + str(self.maxFloor) + \
               '\nthe close time is:' + str(self.closeTime) + '\nthe open time is:' + str(self.openTime) + \
               '\nthe start time is:' + str(self.startTime) + '\nthe stop time is:' + str(self.stopTime)
