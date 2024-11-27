'''Write a program for a matchstick game being played between the computer and a user. Your
program should ensure that the computer always wins. Rules for the game are as follows:
• There are 21 matchsticks.
• The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
• After the person picks, the computer does its picking.
• Whoever is forced to pick up the last matchstick loses the game
'''
# Matchstick game where the computer always wins
ttl = 21  # Total matchsticks

print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\nWelcome to the Matchstick Game!")
print("Rules: Pick 1, 2, 3, or 4 matchsticks. Whoever picks the last matchstick loses.\n--------------------------------------------------------------------------------------")

while ttl > 1:
    # User's turn
    user = int(input("Please pick any number of sticks (1, 2, 3, or 4): "))
    while user not in [1, 2, 3, 4] or user > ttl:  # Validate input
        print("Invalid input. Please pick a number between 1 and 4 within the available matchsticks.")
        user = int(input("Please pick any number of sticks (1, 2, 3, or 4): "))
    ttl -= user
    print(f"Remaining matchsticks: {ttl}")
    
    if ttl == 1:
        print("\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n||\tYou are forced to pick the last matchstick. You lose!\t\t||\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
        break
    
    # Computer's turn
    comp = 5 - user  # Strategic move to leave a multiple of 5
    ttl -= comp
    print(f"Computer picked: {comp}")
    print(f"Remaining matchsticks: {ttl}")
    
    if ttl == 1:
        print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n||\tComputer forces you to pick the last matchstick.You lose!\t\t||\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
        break

