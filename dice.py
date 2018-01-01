import random
from time import sleep 

def lets_roll():
	dice_roll = random.randint(1,int(roll_speed))

	for x in range(dice_roll):
		print 'Dice rolling...'
		sleep(1)
		if x == dice_roll-1:
			print 'Dice landed on %s' % (random.randint(1,6))

print "1 - 10 How hrd do you want to roll?:"
roll_speed = raw_input()

lets_roll()

print "Roll again? (Y/N)"
roll_again = raw_input()

if roll_again == 'Y':
	lets_roll()
else:
	exit()
