import sys


class SCall(object):
    stop_id: int = None
    call_time: float = -1
    floor: int = None  # floor (src/dest)
    arrival_time: float
    pick_up_time: float
    drop_off_time: float
    type = None  # 0 if src, 1 if dest

    def __init__(self, Call, index):
        self.stop_id = (-1) * sys.maxsize
        self.call_time = Call.request_time
        self.drop_off_time = (-1) * sys.maxsize
        self.pick_up_time = (-1) * sys.maxsize
        self.arrival_time = (-1) * sys.maxsize
        self.call_dir: bool = Call.call_dir

    def to_dict(self):
        return {
            'stop_id': self.stop_id,
            'call_time': self.call_time,
            'pick_up_time': self.pick_up_time,
            'drop_off_time': self.drop_off_time
        }


class SrcStop(SCall):
    def __init__(self, Call):
        self.type = 0
        self.floor = Call.srcFloor
        self.arrival_time = self.pick_up_time


class DestStop(SCall):

    def __init__(self, Call):
        self.type = 1
        self.floor = Call.destFloor
        self.arrival_time = self.drop_off_time
