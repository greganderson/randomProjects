def main():
	print "this is a test"
	roll = [1, 2, 4, 2, 2]

def test(roll):
	keep_going = True

	while keep_going:
		answer = raw_input("What do you want to keep: ")
		dice_kept = answer.split()
		dice_kept = map(int, dice_kept)
		(combo, x_times) = getCombos(roll)
		farkle = getComboOrFarkle(roll) == 1500

		# Need to make it so after the for loop is done, you can return.  Don't enter 
		# the for loop if you aren't ready.

		for i in range(1, 7):
			# Stop rolling
			if dice_kept[0] == 0:
				# TODO: Add all dice that are worth points to dice_kept
			# Farkles
			elif farkle:
				return 5
			# Combos
			elif i == combo:
				if i in dice_kept:
					if dice_kept.count(i) != x_times:
						print "You didn't give me all of your dice that were part of a combo."
						break
					else:
						continue
			# Other dice
			else:
				if i in dice_kept and not (i == 1 or i == 5):
					for k in range(roll.count(i)):
						dice_kept.remove(i)

			# If for loop is done and dice_kept is complete, break while loop
			if i == 6:
				keep_going = False

	# Remove the desired dice, and return how many dice are left
	for i in range(len(dice_kept)):
		roll.remove(dice_kept[i])
	return len(roll)
