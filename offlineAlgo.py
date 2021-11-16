from myFunction import *
from Elevator import *
from Building import *


class offlineAlgo:
    jsonFile = 'C:\\Users\\roeyf\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Buildings\\B1.json'
    csvFile = 'C:\\Users\\roeyf\\Documents\\GitHub\\OOP_Ex1\\data\\Ex1_input\\Ex1_Calls\\Calls_a.csv'
    myBuiding = Building(jsonFile, csvFile)
