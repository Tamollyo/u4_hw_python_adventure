# Create your own adventure with python here

def adventure():
    start_game = input("Would you like to start the adventure? Y/N  ")
    if start_game == "Y":
        name = input("Welcome Adventurer, What is your name?")
        location = input("Welcome " + name +
                         " Where would you like to travel?")
        if (len(location) < 5):
            choice1 = input("Dapple choice! " + location +
                            " has great weather. Do you have lodging there? Y/N")
            if choice1 == "Y":
                meal = input(
                    "Wonderful! It's around time for dinner, what are you cooking?")
            else:
                new_meal = input(
                    "Bummer! What kind of lodging do you prefer? ex: hotel, lodge, hostel")
                if (len(new_meal) < 4):
                    lodging = input(
                        new_meal + "is a great choice! How long will you be staying?")
                elif (len(new_meal) >= 4 and len(new_meal) < 8):
                    lodging_two = input(
                        new_meal + "is a great choice!  How long will you be staying?")
                    print("Wow"+lodging_two+" is a long time, have a great stay!")
                    end = input(
                        "This is the end of our adventure, would you like to restart? Y/N")
                    if end == "Y":
                        adventure()
                    else:
                        print("End Game")
                else:
                    lodging_three = input(
                        new_meal + " is a great choice! How long will you be staying?")

        elif (len(location) >= 5 and len(location) < 10):
            choice2 = input("Wonderful choice! " + location +
                            "has great wild grasses. Have you eaten yet today? Y/N")
        else:
            choice2 = input("Spicy choice! " + location +
                            "has great squirrels. What activity do you like to do there?")

    else:
        print("Whoops")
        adventure()


adventure()
