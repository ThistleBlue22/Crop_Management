import random


class Animal:
    """A generic animal"""

    # constructor
    def __init__(self, growth_rate, food_need, water_need):
        self._weight = 1
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Animal"
        self._name = "Bob"

    def needs(self):
        return {'food need': self._food_need, 'water need': self._water_need}

    def report(self):
        return {'type': self._type, 'status': self._status, 'weight': self._weight, 'days growing': self._days_growing}

    def _update_status(self):
        if self._weight > 15:
            self._status = "Old"
        elif self._weight > 10:
            self._status = "Mature"
        elif self._weight > 5:
            self._status = "Young"
        elif self._weight > 0:
            self._status = "Baby"

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
            
        self._days_growing += 1
        self._update_status()


def auto_grow(animal, days):
    for day in range(days):
        food = random.randint(1, 100)
        water = random.randint(1, 10)
        animal.grow(food, water)


def manual_grow(animal):
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-100):\n"))
            if 1 <= food <= 100:
                valid = True
            else:
                print("Value is not valid. Please enter a value between 1 and 100\n")
        except ValueError:
            print("Value is not valid. Please enter a value between 1 and 100\n")

    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10):\n"))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value is not valid. Please enter a value between 1 and 10\n")
        except ValueError:
            print("Value is not valid. Please enter a value between 1 and 10\n")

    animal.grow(food, water)


def menu():
    print("1.Grow the animal Manually")
    print("2.Grow the animal Automatically")
    print("3.Report Status")
    print("0.Exit\n")
    print("Please choose one of the above options")


def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selection:"))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter a valid numerical value. (0-4)")
        except ValueError:
            print("Please enter a valid numerical value. (0-4)")
    return choice


def manage_animal(animal):
    print("This is the animal management program\n")
    noexit = True
    while noexit:
        menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
        elif option == 2:
            auto_grow(animal,30)
        elif option == 3:
            print(animal.report())
        elif option == 0:
            noexit = False
    print("Thank you for using the animal management program")
    
    
def main():
    new_animal = Animal(1,56,7)
    manage_animal(new_animal)


if __name__ == "__main__":
    main()
