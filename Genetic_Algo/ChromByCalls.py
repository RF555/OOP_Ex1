import random
import Call
import myFunction as mf
from Elevator import Elevator
from SCall import SCall, SrcStop, DestStop


def update_q(elev: Elevator, q):
    for i in range(len(q)):
        if i == 0:
            temp_time: float = Elevator.i_to_j_time(elev, 0, q[i].floor)
            q[i].arrival_time = temp_time
            q[i].pick_up_time = temp_time
        else:
            temp: float = Elevator.i_to_j_time(elev, q[i - 1].floor, q[i].floor)
            q[i].arrival_time = q[i - 1].arrival_time + temp
            if type(q[i]) == SrcStop:
                q[i].pick_up_time = q[i].arrival_time
            else:
                q[i].pick_up_time = q[i].arrival_time


class ChromByCalls:
    Calls = []
    Elevs = []
    Allocate = []

    # an array the size of all the calls, each call gets randomly assigned to an elevator

    def __init__(self, Calls: Call, Elevs):
        self.Calls = Calls
        self.Elevs = Elevs
        self.Allocate = [len(Calls)]
        for i in range(len(Calls)):
            is_able = False
            while not is_able:
                counter: int = len(self.Elevs[i].myCalls)
                """
                add a counter for the number of calls for each elevator
                ??? counter < 
                """
                rnd = random.choice(Elevs)
                is_able = self.is_able(i, rnd)
                if is_able:
                    """
                    add limitations on assigning the random Elevator to the i'th call
                    while loop considering the previous calls assigned to the random Elevator
                     
                    """
                    self.Allocate[i] = rnd  # assign the random elevator

    def is_able(self, call_index: int, elev_index: int):
        call = self.Calls[call_index]
        elev = self.Elevs[elev_index]
        if call.call_dir:  # True is UP, False is DOWN
            return mf.pickUpOptionup(elev, call)
        else:
            return mf.pickUpOptiondown(elev, call)

    def chrom_timeline(self, elev_index: int):
        elev: Elevator = self.Elevs[elev_index]
        q = []
        for sc in range(len(self.Allocate)):
            if self.Allocate[sc] == elev_index:
                src: SCall = SrcStop(self.Calls[sc])
                dest: SCall = DestStop(self.Calls[sc])
                if sc == 0:
                    q.append(src)
                    q.append(dest)
                    update_q(elev, q)
                elif q[-1].drop_off_time < src.call_time:
                    q.append(src)
                    q.append(dest)
                    update_q(elev, q)
                else:
                    for isrc in range(len(q), -1):
                        # q[isrc] is UP & arrive to q[isrc] after the new call & q[isrc] is higher than the new src call
                        if q[isrc].call_dir & \
                                (q[isrc].arrival_time > src.call_time) & \
                                (q[isrc].floor > src.floor):
