# Create your own adventure with python here

def adventure():
    start_game = input("Would you like to start the adventure? Y/N  ")
    if start_game == "Y":
        name = input("Welcome Adventurer, What is your name?")
        location = input("Welcome " + name +
                         " Where would you like to travel?")
        if (len(location) < 5):
            choice1 = input("nice choice! " + location +
                            "has great weather. Have you tried their hotdogs? Y/N")
        elif (len(location) >= 5 and len(location) < 10):

        else:

    else:
        print("Whoops")
        adventure()


adventure()
