name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You find yourself laying on the grass in a beautiful meadow. Looking around yourself you find that there are two options in front of you: Go towards the river on your right or go right into the forest on your left. Where are you heading? (left/right): ").lower()

if answer == "right":
    answer = input(
        "You head towards the river. The water is crystal clear and you can't determine how deep it is. Suddenly, you notice several rocks that can serve you to reach the other side of the river. What do you do? (Go back/Use the rocks) ")
    
    if answer == "Go back":
        print("You decide to head back to the forest.")
    elif answer == "Use the rocks":
        print("You are a brave one! You jump on the first rock. Then, on the second, on the third. And... then you fall into the deep waters and drown.")
    else:
        print("Not a valid option. You lose.")

elif answer == "left":
    answer = input(
        "You go deep into the forest. After a while you notice something or someone moving through the shadows of the trees. Do you keep walking forward or do you hide and wait for the thing to approach? (Go forward/Hide): ")
    
    if answer == "Go forward":
        print("You continue walking forward. As you are moving through the trees, someone jumps on your back and you find yourself laying on the ground. You only manage to take a peek at their distorted face before they slit your throath. You die.")
    elif answer == "Hide":
        answer = input(
            "You manage to hide in the trunk of a large oak tree. You patiently wait until a humanoid figure appears from the shadows. It looks like a... live corpse! It walks around the tree where you are hiding. Sniffing like a dog. Do you try to behead it with your sword or do you stay put? (Kill/Stay put): ")
        
        if answer == "Kill":
            print("You jump from behind the walking corpse and swing your sword. WHAT?!?! Where did it go? It turns out that this zombie has superhuman capabilities. It is too fast for you to catch and you find yourself laying on the ground under your distorted friend. You die and get eaten by a walking corpose")
        elif answer == "Stay put":
            print("You hold your breath and pray to God for this zombie to not find you. After a few more sniffs, it dissapears in the forest. You rush to get out of this forest which turned out to be cursed. Good for you!")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose.')
    
print("Thank you got trying", name)