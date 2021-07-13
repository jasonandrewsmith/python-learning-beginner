import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1,6)

p1 = input("enter player 1's name: ")
p2 = input("enter player 2's name: ")

roll1 = roll_dice()
roll2 = roll_dice()

print(p1, "rolled", roll1)
print(p2, "rolled", roll2)

if roll1 > roll2:
    print(p1, "wins!")
elif roll1 < roll2:
    print(p2, "wins!")
else:
    print("it's a tie!")
