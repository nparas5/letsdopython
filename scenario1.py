class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def within_boundary(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

class Car:
    def __init__(self, name, x, y, direction):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, field):
        if self.direction == "N":
            if field.within_boundary(self.x, self.y + 1):
                self.y += 1
        elif self.direction == "S":
            if field.within_boundary(self.x, self.y - 1):
                self.y -= 1
        elif self.direction == "E":
            if field.within_boundary(self.x + 1, self.y):
                self.x += 1
        elif self.direction == "W":
            if field.within_boundary(self.x - 1, self.y):
                self.x -= 1

    def rotate_left(self):
        directions = {"N": "W", "W": "S", "S": "E", "E": "N"}
        self.direction = directions[self.direction]

    def rotate_right(self):
        directions = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.direction = directions[self.direction]

class Simulation:
    def __init__(self, width, height):
        self.field = Field(width, height)
        self.cars = {}

    def add_car(self, name, x, y, direction):
        self.cars[name] = Car(name, x, y, direction)

    def run_simulation(self):
        for name, car in self.cars.items():
            commands = input(f"Please enter commands for car {name}: ")
            for command in commands:
                if command == "F":
                    car.move(self.field)
                elif command == "L":
                    car.rotate_left()
                elif command == "R":
                    car.rotate_right()

            print(f"Your current list of cars are:\n- {car.name}, ({car.x},{car.y}) {car.direction}")

        print("Please choose from the following options:")
        print("[1] Start Over")
        print("[2] Exit")

        option = input()
        if option == "1":
            return True
        elif option == "2":
            print("Thank you for running the simulation. Goodbye!")
            return False

def main():
    print("Welcome to Auto Driving Car Simulation!")
    width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split(','))
    print(f"You have created a field of {width} * {height}.")

    simulation = Simulation(width, height)

    while True:
        print("Please choose from the following options:")
        print("[1] Add a car to field.")
        print("[2] Run Simulation.")
        print("[3] Exit.")

        option = input()
        if option == "1":
            name = input("Please enter the name of the car: ")
            x, y, direction = input("Please enter initial position of car in x y direction format: ").split()
            simulation.add_car(name, int(x), int(y), direction)
        elif option == "2":
            if not simulation.run_simulation():
                break
        elif option == "3":
            print("Thank you for running the simulation. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
