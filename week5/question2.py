class Vehicle:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def move(self):
        return f"{self._name} is moving."

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def move(self):  # Polymorphic method
        return f"{self._name} is driving on the road 🚗."

class Plane(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def move(self):  # Polymorphic method
        return f"{self._name} is flying in the sky ✈️."

# Test the classes
if __name__ == "__main__":
    vehicle = Vehicle("Generic Vehicle")
    car = Car("Toyota")
    plane = Plane("Boeing 747")

    print(vehicle.move())
    print(car.move())
    print(plane.move())