from wheat import *
from potato import *


def display_menu():
    print("Which crop would you like to create?\n")
    print("1.Potato")
    print("2.Wheat\n")
    print("Please select an option from above")


def select_option():
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option Selected: "))
            if choice in (1, 2):
                valid_option = True
            else:
                print("Please enter a valid option!")
        except ValueError:
            print("Please enter a valid option!")

    return choice


def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    return new_crop


def main():
    new_crop = create_crop()
    manage_crop(new_crop)


if __name__ == "__main__":
    main()
