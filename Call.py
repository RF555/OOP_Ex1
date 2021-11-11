class Call:
    elevIndex: int = None
    elevStatus: int = None
    req_time: float = None
    index: int = None
    srcFloor: int = None
    destFloor: int = None

    def __init__(self, index, time, srcFloor, destFloor, elevStatus, elevIndex):
        self.elevIndex = elevIndex
        self.elevStatus = elevStatus
        self.req_time = time
        self.index = index
        self.srcFloor = srcFloor
        self.destFloor = destFloor
