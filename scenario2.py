class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def within_boundary(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

class Car:
    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.index = 0

    def move(self, field):
        if self.index >= len(self.commands):
            return

        command = self.commands[self.index]
        if command == "F":
            if self.direction == "N" and field.within_boundary(self.x, self.y + 1):
                self.y += 1
            elif self.direction == "S" and field.within_boundary(self.x, self.y - 1):
                self.y -= 1
            elif self.direction == "E" and field.within_boundary(self.x + 1, self.y):
                self.x += 1
            elif self.direction == "W" and field.within_boundary(self.x - 1, self.y):
                self.x -= 1

        self.index += 1

    def rotate_left(self):
        directions = {"N": "W", "W": "S", "S": "E", "E": "N"}
        self.direction = directions[self.direction]

    def rotate_right(self):
        directions = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.direction = directions[self.direction]

class Simulation:
    def __init__(self, width, height):
        self.field = Field(width, height)
        self.cars = []

    def add_car(self, name, x, y, direction, commands):
        self.cars.append(Car(name, x, y, direction, commands))

    def run_simulation(self):
        for car in self.cars:
            while car.index < len(car.commands):
                car.move(self.field)
                if self.check_collision(car):
                    break

        print("Your current list of cars are:")
        for car in self.cars:
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")

        print("Please choose from the following options:")
        print("[1] Start Over")
        print("[2] Exit")

        option = input()
        if option == "1":
            return True
        elif option == "2":
            print("Thank you for running the simulation. Goodbye!")
            return False

    def check_collision(self, current_car):
        for car in self.cars:
            if car != current_car and car.x == current_car.x and car.y == current_car.y:
                print(f"-{car.name}, collides with {current_car.name} at ({car.x},{car.y}) at step {current_car.index}")
                return True
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
            commands = input("Please enter the commands for car: ")
            simulation.add_car(name, int(x), int(y), direction, commands)
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
