import json

from models.car import Car
from models.colors import set_color, reset_color
from models.truck import Truck
from models.vehicle import Vehicle
import models.colors


class Garage:
    def __init__(self) -> None:
        self.vehicles = []
        self.load_garage()

    def add_vehicle(self, vehicle) -> None:
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle) -> None:
        self.vehicles.remove(vehicle)

    def list_vehicles(self, colored=False, numbered = False) -> None:
        i = 0
        for vehicle in self.vehicles:
            if colored:
                set_color(vehicle.color)

            if numbered:
                print(f"[{i}]: ", end='')
                i += 1
            print(vehicle)
            if colored:
                reset_color()

    def save_garage(self) -> None:
        with open('garage.json', 'w') as f:
            json.dump([vehicle.__dict__ for vehicle in self.vehicles], f, indent=4)

    def load_garage(self) -> None:
        try:
            with open('garage.json', 'r') as f:
                data = json.load(f)
                if data:
                    for vehicle in data:
                        if 'towing_capacity' in vehicle:
                            self.vehicles.append(Truck(vehicle['make'], vehicle['model'], vehicle['year'], vehicle['color'], vehicle['weight'], vehicle['towing_capacity'], vehicle['id']))
                        elif 'num_doors' in vehicle:
                            self.vehicles.append(Car(vehicle['make'], vehicle['model'], vehicle['year'], vehicle['color'], vehicle['num_doors'], vehicle['id']))
                        else:
                            self.vehicles.append(Vehicle(vehicle['make'], vehicle['model'], vehicle['year'], vehicle['color'], vehicle['id']))
        except json.decoder.JSONDecodeError:
            self.vehicles = []

    def get_vehicle(self, id) -> Vehicle:
        for vehicle in self.vehicles:
            if vehicle.id == id:
                return vehicle
        return None
