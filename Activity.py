class Vehicle:
    def move(self):
        raise NotImplementedError(
            "This method should be overridden by subclasses.")


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"
