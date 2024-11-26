'''Write a program for a matchstick game being played between the computer and a user. Your
program should ensure that the computer always wins. Rules for the game are as follows:
• There are 21 matchsticks.
• The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
• After the person picks, the computer does its picking.
• Whoever is forced to pick up the last matchstick loses the game
'''
import random
ttl=21
while (ttl!=0):
    user=int(input("Please pick any number of stick '1', '2', '3',or'4' : "))
    ttl-=user
    if(ttl>4):
        user=int(input("Please pick any number of stick '1', '2', '3',or'4' : "))
        ttl-=user
    comp=random.randint(1,4)
    ttl-=comp
    print("Computer picked: ",comp)
