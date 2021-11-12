class Elevator:
    flag: bool

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
        self.curr = 0

    # def getid(self):
    #      return self.elevid
    #
    # def getspeed(self):
    #      return self.speed
    #
    # def getminfloor(self):
    #     return self.minFloor
    #
    # def getmaxfloor(self):
    #     return self.maxFloor
    #
    # def getclosetime(self):
    #     return self.closeTime
    #
    # def getopentime(self):
    #     return self.openTime
    #
    # def getstarttime(self):
    #     return self.startTime
    #
    # def getstoptime(self):
    #     return self.stopTime

    def update_flag(self, SCall):
        if SCall.floor > self.curr:
            self.flag = True  # UP
        else:
            self.flag = False  # DOWN

    def __str__(self):
        return 'This elevator id is:' + str(self.elevid) + '\nthe speed is:' + str(self.speed) + \
               '\nthe min floor is:' + str(self.minFloor) + '\nthe max floor is:' + str(self.maxFloor) + \
               '\nthe close time is:' + str(self.closeTime) + '\nthe open time is:' + str(self.openTime) + \
               '\nthe start time is:' + str(self.startTime) + '\nthe stop time is:' + str(self.stopTime)
