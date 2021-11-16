import Call
import random


class ChromByCalls:
    Calls = None
    Elevs = None
    A = None

    # an array the size of all the calls, each call gets randomly assigned to an elevator

    def __init__(self, Calls: Call, Elevs):
        self.Calls = Calls
        self.Elevs = Elevs
        self.A = [len(Calls)]
        elev_sum = len(Elevs)
        for i in range(len(Calls)):
            rnd = random.random() * 100 * elev_sum
            # int_rnd: int = rnd
            int_rnd = round(rnd)
            """
            add limitations on assigning the random Elevator to the i'th call
            while loop considering the previous calls assigned to the random Elevator
             
            """

            if int_rnd >= 0 & int_rnd < elev_sum:  # assign the random elevator
                self.A = i
            else:
                i -= 1
