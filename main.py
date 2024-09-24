#!/usr/bin/python3
import cmd
from models.garage import Garage
from models.car import Car
from models.truck import Truck
from models.vehicle import Vehicle

class MyCmd(cmd.Cmd):
    garage = Garage()


if __name__ == '__main__':
    MyCmd().cmdloop()
