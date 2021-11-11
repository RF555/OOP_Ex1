class Call:
    elevIndex: int = None
    elevStatus: int = None
    req_time = None
    index: int = None
    srcFloor: int = None
    destFloor: int = None
    CallStatus = 'Waiting'

    def __init__(self, index, time, srcFloor, destFloor, elevStatus, elevIndex):
        self.elevIndex = elevIndex
        self.elevStatus = elevStatus
        self.req_time = time
        self.index = index
        self.srcFloor = srcFloor
        self.destFloor = destFloor

    def __str__(self):
        return "Elevator call," + self.req_time.__str__() + "," + self.srcFloor.__str__() + "," + self.destFloor.__str__() + ',' + self.elevStatus.__str__() + ',' + self.elevIndex.__str__()
