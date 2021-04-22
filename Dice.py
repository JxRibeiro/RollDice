#Simple script to roll dices

import random

def rollDice():
	keepRolling = ''
	while keepRolling != 'n':
		i = int(input('How many dices you want to roll? '))
		for j in range(i):
			
			dice = random.randint(1,6)
			print(f'Dice {j+1}: {dice} ')
		keepRolling = input('Do you want to roll again? (y/n)').lower()
	
rollDice()
