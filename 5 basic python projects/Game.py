name = input("Hey type your name: ")
print("Hello "+ name + ". Welcome to the game.")

should_we_play=input("Do u want to play? ").lower()

if should_we_play == "yes" or should_we_play=="y" or should_we_play=="YES" or should_we_play=="Y":
    print("We'll play")
    weapon= input("Choose a weapon (sword/axe): ").lower()

    direction = input("Do u want to go left or right? (left/right): ").lower()
    if(direction == "left"):
        print("U fell off a cliff. Game over! Try again.")
    elif(direction == "right"):
        choice= input("Okay, now u r on a bridge. Wanna swim? Or cross under it? (swim/cross)")
        if choice == "sword" and weapon == "axe" :
            print("U got eaten by an alligator. You die! Game over!")
        else:
            print("U found the gold & won. ")

else:
    print("We are not playing")
