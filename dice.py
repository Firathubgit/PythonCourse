# Imagine a dice game where you need to get a six to advance. Use the module random
# to simulate a series of rolls with a fair, six-sided dice. Write a program that
# prints the results of the rolls until the first six. The program should then print
# the number of rolls it took, according to the example below.
import random

# 4
# 1
# 3
# 1
# 6
# It took 5 rolls to get a 6.
number_of_attempts = 0
given_amounts_of_throw = 0
dice_number=0

while dice_number != 6:
    number_of_attempts = number_of_attempts + 1
    dice_number = random.randint(0,6)
    print(dice_number)
    
else:

    print(f'Det tog {number_of_attempts} kast att få en 6:a.')

