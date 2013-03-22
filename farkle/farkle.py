import random

def main():

	# TODO: Make it so you can choose how many people are playing
	
	# Two player game
	player_1 = 0
	player_2 = 0
	score = 0
	dice = 5

	while (player_1 < 10000) and (player_2 < 10000):
		(score, dice) = takeTurn(score, dice)
		player_1 += score
		(score, dice) = takeTurn(score, dice)
		player_2 += score


def takeTurn(points, dice):
	# Display previous players score and remaining dice, then ask if player
	# wants to keep score and dice or roll a fresh roll
	print "Previous player's score: " + str(points)
	print "Number of dice remaining: " + str(dice)
	while True:
		try:
			answer = input("Keep score and roll with " + str(dice) + " dice? (1=yes, 0=no) ")
			if (answer != 1) and (answer != 0):
				print "Please only input a 1 or a 0."
			else:
				break
		except SyntaxError:
			print "Please only input a 1 or a 0."

	# Start with all 5 dice

	if answer == 0:
		dice = 5
		points = 0
		roll = rollAll()

		while True:
			points += getPoints(roll)
			if getPoints(roll) == 0:
				print "Rolled: " + str(roll)
				print "Points: 0"
				points = 0
				dice = 0
				return points, dice
			print
			print "Rolled: " + str(roll)
			print "Points: " + str(points)

			dice_kept = keepGoing(roll)
			(combo, x_times) = getCombos(roll)


			# They want to keep going
			if 0 == 0:	# TODO: Fix
				dice = getRemaining(dice_kept, roll)
				if dice == None:
					return points, dice
				elif dice == 0:
					roll = rollAll()
				else:
					roll = rollRemaining(dice)
	else:
		# TODO: Implement
		print "Need to implement"
		return points, dice

def getRemaining(roll):
	keep_going = True

	# Check for farkle
	farkle = isComboOrFarkle(roll) == 1500
	if farkle:
		return 5

	while keep_going:
		answer = raw_input("What do you want to keep: ")
		dice_kept = answer.split()
		dice_kept = map(int, dice_kept)
		(combo, x_times) = getCombos(roll)

		for i in range(1, 7):
			# Stop rolling
			if dice_kept[0] == 0:
				ones = getOnes(roll)
				fives = getFives(roll)
				dice_kept= ""
				if combo == 1 or combo == 5:
					for i in range(ones):
						dice_kept+= "1 "
					for i in range(fives):
						dice_kept+= "5 "
				else:
					for i in range(ones):
						dice_kept+= "1 "
					for i in range(fives):
						dice_kept+= "5 "
					for i in range(x_times):
						dice_kept+= str(combo) + " "
				dice_kept= dice_kept.split()
				dice_kept = map(int, dice_kept)
				keep_going = False
				break
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

	# TODO: Need to recheck getting rid of dice that are not worth points
	# TODO: Need to recheck keeping 2 2 2 in [1, 2, 2, 4, 2], it tries to keep the 1 as well

	# Remove the desired dice, and return how many dice are left
	for i in range(len(dice_kept)):
		roll.remove(dice_kept[i])
	return len(roll)

"""

# Decides whether or not player keeps going, and
# which dice to keep if they are.
def keepGoing(roll):
	# TODO: Possibly add an expression that gets rid of ','
	# TODO: Need to make it so they can only keep dice that are worth points
	(combo, x_times) = getCombos(roll)
	while True:
		dice_kept = raw_input("Which dice would you like to keep, enter 0 to stop (e.g. \"1 1 5\" or \"0\"): ")
		dice_kept = dice_kept.split()
		if ("2" in dice_kept) and combo == 2:
			if dice_kept.count("2") != x_times:
				print "You entered at least one die that isn't worth points."
				continue
			else:
				return dice_kept
		elif ("3" in dice_kept) and combo == 3:
			if dice_kept.count("3") != x_times:
				print "You entered at least one die that isn't worth points."
				continue
			else:
				return dice_kept
		elif ("4" in dice_kept) and combo == 4:
			if dice_kept.count("4") != x_times:
				print "You entered at least one die that isn't worth points."
				continue
			else:
				return dice_kept
		elif ("6" in dice_kept) and combo == 6:
			if dice_kept.count("6") != x_times:
				print "You entered at least one die that isn't worth points."
				continue
			else:
				return dice_kept
		elif isComboOrFarkle(roll) == 1500:
			return dice_kept
		else:
			if dice_kept[0] == "0":
				return dice_kept
			elif "1" in dice_kept:
				return dice_kept
			elif "5" in dice_kept:
				return dice_kept
			print "You entered at least one die that isn't worth points."
			continue



def getRemaining(dice_kept, roll):

	# Pull dice from roll
	for i in range(len(dice_kept)):
		if roll.count(dice_kept) == "0":
			print "You told me to keep dice you didn't have.  Therefore, you shall suffer."
			dice = None
			return dice
		try:
			roll.remove(int(dice_kept[i]))
		except ValueError:
			print "You didn't follow instructions.  Therefore, you shall suffer."
			print "Next time, make sure to keep dice in this format: 1 3 3 3"
			dice = None
			return dice
	dice = len(roll)
	return dice

"""


def getPoints(roll):
	combo = isComboOrFarkle(roll)
	if combo == None:
		total = (getOnes(roll) * 100) + (getFives(roll) * 50)
	elif combo == 1500:
		total = combo
	else:
		if getOnes(roll) >= 3:
			total = combo + (getFives(roll) * 50)
		elif getFives(roll) >= 3:
			total = combo + (getOnes(roll) * 100)
		else:
			total = combo + (getOnes(roll) * 100) + (getFives(roll) * 50)
	return total


def rollAll():
	roll = []
	for i in range(5):
		roll.append(rollDie())
	return roll


def rollRemaining(num):
	roll = []
	for i in range(num):
		roll.append(rollDie())
	return roll


def rollDie():
	return random.randrange(1, 7)


def getOnes(roll):
	return roll.count(1)


def getFives(roll):
	return roll.count(5)


# Returns combos as: (combo, x_times) where combo is the number
# of the combo, and x_times is how many dice there were to make
# this combo
def getCombos(roll):
	# Count for each number the dice have rolled
	b = []
	for i in range(1, 7):
		b.append(roll.count(i))

	# Check for combos
	for i in range(6):
		if b[i] == 3:
			return i+1, 3
		if b[i] == 4:
			return i+1, 4
		if b[i] == 5:
			return i+1, 5
	# TODO: Check to see if this causes problems
	return 0, 0


def isComboOrFarkle(roll):
	# Count for each number the dice have rolled
	one = roll.count(1)
	two = roll.count(2)
	three = roll.count(3)
	four = roll.count(4)
	five = roll.count(5)
	six = roll.count(6)

	# Check for farkle
	if (one == 1 and two == 1 and three == 1 and four == 1 and five == 1) or (two == 1 and three == 1 and four == 1 and five == 1 and six == 1):
		return 1500

	(combo, x_times) = getCombos(roll)
	if combo == 1:
		if x_times == 3:
			return combo * 1000
		else:
			return combo * 1000 * (2*(x_times-3))
	else:
		if x_times == 3:
			return combo * 100
		else:
			return combo * 100 * (2*(x_times-3))


def findNumberOfFarkles(num):
	# Test how many farkles are rolled in given number of rolls
	total = 0
	for i in range(num):
		roll = rollAll()
		if isComboOrFarkle(roll) == 1500:
			total += 1
	return total


#main()
