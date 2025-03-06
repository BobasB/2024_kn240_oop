from abc import ABC, abstractmethod

# Абстрактний клас
class Vehicle(ABC):
    def __init__(self, brand: str):
        self.brand = brand

    @abstractmethod
    def move(self):
        """Абстрактний метод, який має бути реалізований у підкласах"""
        pass

# Дочірній клас Car реалізує абстрактний метод move
class Car(Vehicle):
    def move(self):
        return f"{self.brand} рухається по дорозі."

# Дочірній клас Boat реалізує абстрактний метод move
class Boat(Vehicle):
    def move(self):
        return f"{self.brand} пливе по воді."

# Дочірній клас Airplane реалізує абстрактний метод move
class Airplane(Vehicle):
    def move(self):
        return f"{self.brand} летить у повітрі."

# Демонстрація роботи
vehicles = [Car("Tesla"), Boat("Yamaha"), Airplane("Boeing")]

for vehicle in vehicles:
    print(vehicle.move())
