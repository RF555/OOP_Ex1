import random

import Call


class ChromByElevator:
    Calls = None
    Elev = None
    A = None

    def __init__(self, Calls: Call, Elev):
        self.Calls = Calls
        self.Elev = Elev
        self.A = [len(Calls)]
        for i in range(len(Calls)):
            rand = random.random()
            if rand >= 0.5:
                self.A[i] = 0
            else:
                self.A[i] = 1

    def value(self):
        total_wait_time = 0
        curr_calls = 0
        for i in range(len(self.A)):
            if self.A[i] == 1:
                curr_calls += 1
                total_wait_time += self.dest_call_time(self.Calls[i]) - self.Calls[i].requset_time
        return total_wait_time / curr_calls

    def dest_call_time(self, i):
        c = self.Calls[i]
        e = self.Elev
        c_time = 0
        if i == 0:
            return 0
        for j in range(i + 1):
            if self.A[i] == 1:


        ?????
