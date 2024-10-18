# Task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest! ")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You found a hidden treasure!")
else: 
    print("Please choose a path")

# task 2

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest! ")
    elif action == "cross a river":
        print("You found a boat!")

elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("the torch illuminates the surrounding revealing a path")
    elif action == "proceed in the dark":
        print("you venture the cave in complete darkness, disoriented you take the wrong path leading you into bottomless pit.")
    else:
        print("undecided, you stand still at the entrance of the cave.")   
        pass

# Task 1

attendees = int(input("Enter the number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(f"recommended : {venue}")

# Task 2

if attendees > 50:
    print("we recommend : audio system ")
if attendees < 20:
    print("we recommend: projector")

food = input("Would you like any vegetarian options? (yes/no): ")
if food == 'yes':
    print("we highly recommend our Veggie Delight Caterers!")
else: 
    print("Gourmet Meals Caterers.")