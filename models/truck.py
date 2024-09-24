from models.vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, make, model, year, color, weight, towing_capacity, id=None):
        super().__init__(make, model, year, color)
        self.weight = weight
        self.towing_capacity = towing_capacity

    def __str__(self):
        return f"{super().__str__()} weighing {self.weight} lbs with a towing capacity of {self.towing_capacity} lbs"
