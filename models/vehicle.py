import json
import uuid


class Vehicle:
    def __init__(self, make, model, year, color, id=None):
        if id is None:
            id = uuid.uuid4()
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.id = str(id)

    def __str__(self):
        return f"{self.id} - {self.year} {self.make} {self.model} in {self.color}"
