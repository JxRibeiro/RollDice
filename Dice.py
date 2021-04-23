#Simple script to roll dices
import random
def rollDice():
	keepRolling = ''
	while keepRolling != 'n':
		diceSum = 0
		i = int(input('How many dices you want to roll? '))
		for j in range(i):	
			dice = random.randint(1,6)
			diceSum = diceSum + dice
			print(f'Dice {j+1}: {dice} ')
		print(f'Dice sum: {diceSum}')
		keepRolling = input('Do you want to roll again? (y/n)').lower()
rollDice()
