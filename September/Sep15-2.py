name = input("Enter your name: ")
print("Welcome", name, 'to this adventure game!')

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == 'left': 
    answer = input("You turned left and reached a river. You can walk around it or swim across it. Type 'walk' to walk and 'swim' to swim. ")

    if answer == 'swim':
        print('You swam in the river and got eaten by the alligator.')
        print("You lose")
    elif answer == 'walk':
        print("You walked for many hours and ran out of water.")
        print("You loose")
elif answer == 'right': 
    answer = input("You reached an old bridge. It looks wobbly. Do you want to cross it or head back (cross/back)? ")
    if answer == 'back':
        print('You went to the main road')
        print("You lose")
    elif answer == 'cross':
        answer = input("You crossed the bridge and met a stranger. Do you want to talk to him (yes/no)? ")

        if answer == 'yes':
            print("The stranger told you the secret for being the richest person")
            print("You win")
        elif answer == 'no':
            print("You ignore the stranger and is killed by him")
            print('You lose')
        else:
            print("Invalid option. You lose")
else: 
    print("Invalid option. You lose")

print("Hope you enjoyed the game", name)