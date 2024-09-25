#!/usr/bin/python3
import cmd
from platform import system

from models import garage
from models.garage import Garage
from models.car import Car
from models.truck import Truck
from models.vehicle import Vehicle
import webbrowser
from os import system

class MyCmd(cmd.Cmd):
    garage = Garage()

    def __init__(self):
        super().__init__()
        self.intro = 'Type "help" or "?" for a list of commands.'

    @staticmethod
    def do_exit(self):
        """
Quit the program.
Usage: exit
        """
        return True

    @staticmethod
    def do_EOF(self):
        print()
        return True

    def do_roll(self, arg):
        """
lets you take your car for a roll
Usage: roll
        """
        self.garage.list_vehicles(True, True)

        print("Type the number or the id next to the vehicle you want to drive.")
        input()
        print("Going for a roll...")
        # webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        system("rickroll")  # only works on my device, but this would fullscreen rickroll you in the VLC Media player

    def do_add(self, arg):
        """
initiates a dialog for adding a vehicle of the given type.
vehicle_type: "car" or "truck". Not case sensitive.
Usage: add
        """
        print("Adding a vehicle to garage...\n")
        type = input("('Car' or 'Truck')\nVehicle type: ").capitalize()
        if type != "Car" and type != "Truck":
            print("Please specify a valid vehicle type. (Car or Truck)")
            return
        make = input("Make: ")
        model = input("Model: ")
        year = input("Year: ")
        color = input("Color: ")
        if type == "Car":
            num_doors = input("Number of doors: ")
            new_vehicle = Car(make, model, year, color, num_doors)
        else:
            weight = input("Weight: ")
            towing_capacity = input("Towing capacity: ")
            new_vehicle = Truck(make, model, year, color, weight, towing_capacity)
        print(f"\nDone! Adding to garage: {str(new_vehicle)}")
        self.garage.add_vehicle(new_vehicle)
        self.garage.save_garage()

    def do_remove(self, arg):
        """
Prompts a list of vehicles in garage and removes a given vehicle from the garage.
Usage: remove
        """
        i = 0
        self.garage.list_vehicles(True, True)

        print("type the number or the id next to the vehicle you want to remove.")
        user_input = input()
        if user_input.isdigit():
            if 0 <= int(user_input) < len(self.garage.vehicles):
                print(f"Removing {self.garage.vehicles[int(user_input)]}...")
                self.garage.remove_vehicle(self.garage.vehicles[int(user_input)])
                self.garage.save_garage()
            else:
                print("Invalid index provided.")
        else:
            for vehicle in self.garage.vehicles:
                if vehicle.id == user_input:
                    print(f"Removing {vehicle}...")
                    self.garage.remove_vehicle(vehicle)
                    self.garage.save_garage()
                    return
            print("No vehicle found with that id.")
            return


    def do_list(self, arguments = "True False"):
        """
Lists all vehicles in the garage.
colored: determines whether to automatically color some entries based on the vehicle's color. Valid values: True/False/1/0/Default (optional unless Numbered is given, in which case, use Default to leave default). Default: True.
numbered: determines whether to add a number before the entry (i.e. [<number>]: <vehicle info>). Valid values: True/False/1/0/Default. Default: False.
Usage: list <colored> <numbered>
        """
        args= arguments.split(" ")
        colored = True
        numbered = False
        if len(args) >= 1 and args[0] != '':
            if args[0].lower() == "true" or args[0].lower() == "1" or args[0].lower() == "default":
                colored = True
            elif args[0].lower() == "false" or args[0].lower() == "0":
                colored = False
            else:
                print("Please enter true, false, 1, 0, or default for parameter colored. Usage: list <colored> <numbered>")
                return
        if len(args) >= 2:
            if args[1].lower() == "true" or args[1].lower() == "1":
                numbered = True
            elif args[1].lower() == "false" or args[1].lower() == "0" or args[1].lower() == "default":
                numbered = False
            else:
                print("Please enter true, false, 1, 0, or default for parameter numbered. Usage: list <colored> <numbered>")
                return
        print("Listing vehicles in garage:")        
        self.garage.list_vehicles(colored, numbered)


if __name__ == '__main__':
    MyCmd().cmdloop()
