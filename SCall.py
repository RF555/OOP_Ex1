import sys


class SCall(object):
    stop_id: int = None
    call_time: float = None
    floor: int = None  # floor (src/dest)
    type = None  # 0 if src, 1 if dest

    def __init__(self, Call, index):
        self.stop_id = (-1) * sys.maxsize
        self.call_time = Call.request_time
        self.drop_off_time: float = (-1) * sys.maxsize
        self.pick_up_time = (-1) * sys.maxsize


class SrcStop(SCall):
    def __init__(self, Call):
        self.type = 0
        self.floor = Call.srcFloor


class DestStop(SCall):

    def __init__(self, Call):
        self.type = 1
        self.floor = Call.destFloor
