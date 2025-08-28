class Superhero:
    def __init__(self, name, power):
        self._name = name  # Protected attribute
        self._power = power  # Protected attribute
        self._missions = 0

    def get_name(self):
        return self._name

    def show_info(self):
        return f"Hero: {self._name}, Power: {self._power}, Missions: {self._missions}"

    def do_mission(self):
        self._missions += 1
        return f"{self._name} completed a mission!"

    def use_power(self):
        return f"{self._name} uses {self._power} power!"

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self._speed = speed  # Protected attribute

    def use_power(self):  # Override for polymorphism
        return f"{self._name} flies with {self._power} power at {self._speed} mph!"

    def fly(self, place):
        return f"{self._name} flies to {place}!"

# Test the classes
if __name__ == "__main__":
    hero1 = Superhero("Thunder", "Strength")
    print(hero1.show_info())
    print(hero1.use_power())
    print(hero1.do_mission())

    hero2 = FlyingSuperhero("Skywing", "Flight", 200)
    print(hero2.show_info())
    print(hero2.use_power())
    print(hero2.fly("City"))