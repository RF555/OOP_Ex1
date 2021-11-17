import Call
import random

from Elevator import Elevator


class ChromByCalls:
    Calls: Call = []
    Elevs: Elevator = []
    Allocate: int = []

    # an array the size of all the calls, each call gets randomly assigned to an elevator

    def __init__(self, Calls: Call, Elevs):
        self.Calls = Calls
        self.Elevs = Elevs
        self.Allocate = [len(Calls)]
        for i in range(len(Calls)):
            counter: int = len(self.Elevs.)
            """
            add a counter for the number of calls for each elevator
            ??? counter < 
            """
            rnd = random.choice(Elevs)
            """
            add limitations on assigning the random Elevator to the i'th call
            while loop considering the previous calls assigned to the random Elevator
             
            """
            self.Allocate[i] = rnd  # assign the random elevator


def is_able(self, call_index: int, elev_index: int):
    call = self.Calls[call_index]
    elev = self.Elevs[elev_index]
