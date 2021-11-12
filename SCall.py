import sys


class SCall(object):
    stop_id = None
    time = None
    floor = None  # floor (src/dest)
    type = None  # 0 if src, 1 if dest

    def __init__(self, Call):
        self.stop_id = (-1) * sys.maxsize
        self.time = Call.req_time


class SrcStop(SCall):
    def __init__(self, Call):
        self.type = 0
        self.floor = Call.srcFloor


class DestStop(SCall):
    def __init__(self, Call):
        self.type = 1
        self.floor = Call.destFloor
