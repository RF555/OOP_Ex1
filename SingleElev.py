class SinglgeElev:

    def __init__(self, UpCalls, DownCalls, elevid, speed, minfloor, maxfloor, closetime, opentime, starttime, stoptime):
        self.elevid = elevid
        self.speed = speed
        self.minFloor = minfloor
        self.maxFloor = maxfloor
        self.closeTime = closetime
        self.openTime = opentime
        self.startTime = starttime
        self.stopTime = stoptime
        self.UpCalls = UpCalls
        self.DownCalls = DownCalls

    def my_calls(self):
