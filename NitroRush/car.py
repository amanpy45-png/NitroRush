class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10


car1 = Car("Red Car", 50)

print(car1.name)
print(car1.speed)

car1.accelerate()

print(car1.speed)

car2 = Car("Blue Car", 80)
print(car2.name)
print(car2.speed)

car1.accelerate()
print(car2.speed)
