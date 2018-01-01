import random

dice_roll = random.randint(3,30)

for x in range(dice_roll):
	print 'Dice rolling...'
	if x == dice_roll-1:
		print 'Dice landed on %s' % (random.randint(1,6))
