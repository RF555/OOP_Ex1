class Call:
    elevIndex: int = None
    elevStatus: int = None
    request_time = None
    allocatedElev: int = None
    srcFloor: int
    destFloor: int
    CallStatus = 'Waiting'
    # change call_dir to int: 1 is UP, -1 is DOWN, 0 is LEVEL
    is_up: bool  # if call is UP- TRUE, if call is DOWN- FALSE
    is_down: bool  # if call is UP- TRUE, if call is DOWN- FALSE

    def __init__(self, request_time, srcFloor, destFloor, elevStatus, elevIndex, allocatedElev):
        self.elevIndex = elevIndex
        self.elevStatus = elevStatus
        self.request_time = request_time
        self.allocatedElev = allocatedElev
        self.srcFloor = srcFloor
        self.destFloor = destFloor
        self.is_up = (int(self.srcFloor) < int(self.destFloor))
        self.is_down = (int(self.srcFloor) > int(self.destFloor))

    def __str__(self):
        return "Elevator call," + self.request_time.__str__() + "," + self.srcFloor.__str__() + "," + self.destFloor.__str__() + ',' + self.elevStatus.__str__() + ',' + self.allocatedElev.__str__()

    def changeallocatedelev(self, elevNumber):
        self.allocatedElev = elevNumber
