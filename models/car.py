import uuid
from models.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, make, model, year, color, num_doors, id = None):
        super().__init__(make, model, year, color, id)
        self.num_doors = num_doors

    def __str__(self):
        return f"{super().__str__()} with {self.num_doors} doors"
