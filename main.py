# Create your own adventure with python here
def start():
    start_game = input("Would you like to start the adventure? Y/N")
    if start_game == "Y":
        adventure()
    else:
        print("Whoops")
        start()


def adventure():
    name = input("Welcome Adventurer, What is your name?")
    location = input("Welcome " + name + " Where would you like to travel?")
