# Adrian Posada
# Oct. 7, 2021
# 2:10 p.m.
# My Camel Game

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20
canteen = 0

while done == False:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    user_choice = input("What is your choice? ")

    if user_choice.upper() == "Q":
        done = True
    elif user_choice.upper() == "E":
        print("Miles traveled: " + str(miles_traveled))
        print("Drinks: " + str(drinks))
        print("Natives distance: ")
