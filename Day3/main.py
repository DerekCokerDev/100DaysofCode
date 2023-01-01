print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right.\"\n")

if direction.lower() == "left":
    decision = input("You arrived at a river bank with another island in the distance. Do you wait on a boat or swim across? Type \"wait\" or \"swim.\"\n")
    if decision.lower() == "wait":
        door_color = input("You arrived at a mansion with 3 doors. The doors are red, yellow, and blue. Which do you choose? Type \"red\", \"yellow\", or \"blue.\"\n")
        if door_color.lower() == "yellow":
            print("You have escaped to the wild blue yonder!!")
        elif door_color.lower() == "blue":
            print("You were shot by a cross bow waiting to fire. Game Over!!")
        else:
            print("Flames engulfed you. Gave over!!")
    else:
        print("You were attacked by a shark. Game over!!")
else:
    print("You fell into a sink hole and suffocated. Gave over!!")
