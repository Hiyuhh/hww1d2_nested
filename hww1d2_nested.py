# 1. Nested Decisions: The Adventure Game
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass #Default Path
elif place == "cave":
    print("You find a hidden treasure!")
    # Task 2: Setting the Scene
    action = input("you continue down the cave: light a torch or proceed in the dark?")
    if action == "light a torch":
        print("you woke up all the bats! RUN!")
    elif action == "proceed in the dark":
        print("you found a cave full of rare glowing crystals! JACKPOT")
    else:
        pass #Default Path
else:
    pass #Default Path
#im pretty sure i do not know how to use the (pass) come back to it 
 
# 2. Quick Decisions: The Event Planner 
    # Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
if int(attendees > 100):
    print("large hall")
    addons = input("Would you like to add an audio system with your event? yes or no?")
    if addons == "yes":
        print("Great!!")
    elif addons == "no":
        print("If you change your mind, you can add it at any time! :D")
elif attendees <= 100:
    print("conference room")
    #Task 2: Venue Selection
    addons = input("Would you like to add a projector with your event? yes or no?")
    if addons == "yes":
        print("Awesome!")
    elif addons == "no":
        print("That's okay! let us know if you change your mind ^-^")

# Task 3: Catering Choices
meal = input("Would you like a vegetarian meal? yes or no?")
if meal == "yes":
    print("We recommend the Veggie Delight Caterers")
elif meal == "no":
    print("For a non-vegetarian meal we recommend the Gourmet Meals Caterers")
    
