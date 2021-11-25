import random
import Call
import myFunction as mf
from Elevator import Elevator
from SCall import SCall, SrcStop, DestStop


def update_q(elev: Elevator, q, start_index):
    for i in range(start_index, len(q) - 1):
        if i == 0:
            temp_time: float = Elevator.i_to_j_time(elev, 0, q[i].floor)
            q[i].arrival_time = temp_time
            q[i].pick_up_time = temp_time
        elif q[i].floor == q[i - 1].floor:
            q[i].arrival_time = q[i - 1].arrival_time
        else:
            temp: float = Elevator.i_to_j_time(elev, q[i - 1].floor, q[i].floor)
            q[i].arrival_time = q[i - 1].arrival_time + temp
            if q[i].type == 0:  # is SrcStop
                q[i].pick_up_time = q[i].arrival_time
            else:
                q[i].drop_off_time = q[i].arrival_time


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
        return mf.pick_up_option(elev, call)

    def chrom_timeline(self, elev_index: int):
        elev: Elevator = self.Elevs[elev_index]
        q = []
        for sc in range(len(self.Allocate) - 1):
            if self.Allocate[sc] == elev_index:
                src: SCall = SrcStop(self.Calls[sc])
                dest: SCall = DestStop(self.Calls[sc])
                # the first stop -> add both
                if sc == 0:
                    q.append(src)
                    q.append(dest)
                    update_q(elev, q, len(q) - 1)
                # the call is requested after the arrival time for the last SCall -> add both to the end
                elif q[-1].drop_off_time < src.call_time:
                    q.append(src)
                    q.append(dest)
                    update_q(elev, q, len(q) - 1)
                else:
                    for i_src in range(len(q) - 1, -1):
                        # q[i_src] is UP & arrive to q[i_src] after the new call &
                        # q[i_src] is higher than the new src call & src is UP
                        if q[i_src].is_up & \
                                (q[i_src].arrival_time > src.call_time) & \
                                (q[i_src].floor >= src.floor) & \
                                src.is_up:
                            """ while loop for the dest allocation, after try other src options"""
                            i_dest = i_src
                            while q[i_dest].is_up & i_src < i_dest:
                                if q[i_dest].is_down:
                                    break
                                else:
                                    if q[i_dest].floor >= dest.floor:
                                        q.insert(i_src, src)
                                        q.insert(i_dest, dest)
                                        update_q(elev, q, i_src - 1)
                                    else:
                                        i_dest += 1
                        # q[i_src] is DOWN & arrive to q[i_src] after the new call &
                        # q[i_src] is lower than the new src call & src is DOWN
                        elif q[i_src].is_down & (q[i_src].arrival_time > src.call_time) & \
                                (q[i_src].floor <= src.floor) & src.is_down:
                            """ while loop for the dest allocation, after try other src options"""
                            i_dest = i_src
                            while q[i_dest].is_down & i_src < i_dest:
                                if q[i_dest].is_up:
                                    break
                                else:
                                    if q[i_dest].floor <= dest.floor:
                                        q.insert(i_src, src)
                                        q.insert(i_dest, dest)
                                        update_q(elev, q, i_src - 1)
                                    else:
                                        i_dest += 1
                        else:
                            q.append(src)
                            q.append(dest)
                            update_q(elev, q, len(q) - 1)