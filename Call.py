class Call:
    elevIndex: int = None
    elevStatus: int = None
    request_time = None
    allocatedElev: int = None
    srcFloor: int = None
    destFloor: int = None
    CallStatus = 'Waiting'
    call_dir: bool  # if call is UP- TRUE, if call is DOWN- FALSE

    def __init__(self, request_time, srcFloor, destFloor, elevStatus, elevIndex, allocatedElev):
        self.elevIndex = elevIndex
        self.elevStatus = elevStatus
        self.request_time = request_time
        self.allocatedElev = allocatedElev
        self.srcFloor = srcFloor
        self.destFloor = destFloor
        self.call_dir = (self.srcFloor < self.destFloor)

    def __str__(self):
        return "Elevator call," + self.request_time.__str__() + "," + self.srcFloor.__str__() + "," + self.destFloor.__str__() + ',' + self.elevStatus.__str__() + ',' + self.elevIndex.__str__()
