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
                if (len(meal) < 5):
                    food = input("EWWW, why would you cook " +
                                 meal + "Do you regret that decision? Y/N")
                    if food == "Y":
                        end = input(
                            "TOO BAD, the " + meal + "killed you. Would you like to restart? Y/N")
                        if end == "Y":
                            adventure()
                        else:
                            print("End Game")
                    elif food == "N":
                        end = input(
                            "WOWZA, the " + meal + "killed you. Would you like to restart? Y/N")
                        if end == "Y":
                            adventure()
                        else:
                            print("End Game")
                elif (len(meal) > 5):
                    food = input("EWWW, why would you cook " + meal)
                    end = input(
                        "You died from that horrible " + meal + " would you like to restart? Y/N")
                    if end == "Y":
                        adventure()
                    else:
                        print("End Game")
            else:
                new_place = input(
                    "Bummer! What kind of lodging do you prefer? ex: hotel, lodge, hostel")
                if (len(new_place) < 4):
                    lodging = input(
                        new_place + "is a great choice! How long will you be staying?")
                    if (int(lodging) < 10):
                        end = input(
                            lodging + " is such a short amount of time would you like to restart? Y/N")
                        if end == "Y":
                            adventure()
                        else:
                            print("End Game")
                    else:
                        end = input(
                            lodging + " is such a weird amount of time would you like to restart? Y/N")
                        if end == "Y":
                            adventure()
                        else:
                            print("End Game")
                elif (len(new_place) >= 4 and len(new_place) < 8):
                    lodging_two = input(
                        new_place + "is a great choice!  How long will you be staying?")
                    print("Wow"+lodging_two+" is a long time, have a great stay!")
                    end = input(
                        "This is the end of our adventure, would you like to restart? Y/N")
                    if end == "Y":
                        adventure()
                    else:
                        print("End Game")
                else:
                    lodging_three = input(
                        new_place + " is a great choice! How long will you be staying?")
                    if (int(lodging_three) < 6):
                        end = input(
                            "What the heck, the place has termites, do you want to leave? Y/N")
                        if end == "Y":
                            adventure()
                        else:
                            print("End Game")
                    else:
                        end = input(
                            "What the heck, bed bugs much? I guess it's time to end the adventure, do you want to restart? Y/N")
                        if end == "Y":
                            adventure()
                        else:
                            print("End Game")

        elif (len(location) >= 5 and len(location) < 10):
            choice2 = input("Wonderful choice! " + location +
                            "has great wild grasses. Have you eaten yet today? Y/N")
            if choice2 == "Y":
                food = input("What would you like to eat?")
                if (len(food) < 6):
                    mild = input("Seems mild, want to take it up a notch? Y/N")
                elif (len(food) >= 6 and len(food) < 10):
                    medium = input("Seems like" + name +
                                   " could take the heat, make it spicier? Y/N")
                else:
                    spicy = input("OOoo I like you" + name +
                                  "You're one spicy human. Add a little sweetness? Y/N")
                    if spicy == "Y":
                        sweet = input(
                            "OOOOOWwwwweeeee time to kick up this flavor train. How about a little honey on your " + food + "Y/N?")
                        if sweet == "Y":
                            end = input(
                                "That's one good meal, do you want to restart? Y/N")
                            if end == "Y":
                                adventure()
                            else:
                                print("End Game")

        else:
            choice3 = input("Spicy choice! " + location +
                            "has great squirrels. What activity do you like to do there?")

    else:
        print("Whoops")
        adventure()


adventure()
