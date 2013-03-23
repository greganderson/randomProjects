import random

def main():

	# TODO: Let the player know if they roll a farkle
	# TODO: Make the actual playing look a lot cleaner
	

	print
	print
	print "Welcome to Farkle!"
	print
	print
	raw_input("Press enter for instructions:")
	print
	print
	showInstructions()

	# Get number of players
	numPlayers = input("Number of players: ")
	# List of players, stored as a duple: (playerName, score)
	players = []

	# Get names for each player
	print "\nNames for each player\n"
	for i in range(1, numPlayers+1):
		name = raw_input("Player " + str(i) + ": ")
		print
		players.append((name, 0, i-1))

	# Initialize the score and dice variables
	score = 0
	dice = 5

	# Play the game
	while not getWinner(players):
		for player in players:
			print "\n\n" + player[0] + " -> " + str(player[1]) + "\n\n"
			(score, dice) = takeTurn(score, dice)
			addScore(players, player[0], player[1], player[2], score)

	# Get the winner and display their glory!
	winner = finalWinner(players)
	print "\n\n" + winner[0] + " wins with " + str(winner[1]) + " points!\n\n"


# Goes through a players full turn.
def takeTurn(points, dice):
	# Display previous players score and remaining dice, then ask if player
	# wants to keep score and dice or roll a fresh roll
	print
	print "Previous player's score: " + str(points)
	print "Number of dice remaining: " + str(dice)
	print

	keep_previous = False

	if points != 0:
		try:
			answer = input("Keep players score and roll with " + str(dice) + " dice? (1=yes, 0=no) ")
			if answer == 0:
				points = 0
				dice = 5
			elif answer == 1:
				keep_previous = True
			else:
				print "Please only input a 1 or a 0."
		except NameError:
			print "Please only input a 1 or a 0."
		
		

	while True:
		try:
			if not keep_previous:
				print
				print "Points: " + str(points)
				print
				answer = input("Keep score and roll with " + str(dice) + " dice? (1=yes, 0=no) ")
			else:
				answer = 1
				keep_previous = False

			# Keep rolling
			if answer == 1:
				roll = rollRemaining(dice)
				print
				print "Rolled " + str(roll)
				print
				rollPoints = getPoints(roll)

				# No points were rolled, therefore end of turn
				if rollPoints == 0:
					return (0, 5)

				dice_kept = chooseDiceToKeep(roll)
				points += getPoints(dice_kept)
				dice = getRemaining(roll, dice_kept)
				
			# Keep points
			elif answer == 0:
				return points, dice
			else:
				print "Please only input a 1 or a 0."
		except NameError:
			print "Please only input a 1 or a 0."
	






# Returns the number of dice left over after a
# player chooses which dice to keep
def getRemaining(roll, dice_kept):

	# Remove the desired dice, and return how many dice are left
	for e in dice_kept:
		roll.remove(e)
	# All dice had points, so reset to 5
	if len(roll) == 0:
		return 5
	return len(roll)


# Returns all of the dice that give points
def getPointDice(roll):
	(combo, x_times) = getCombos(roll)

	# Remove all non-point-yielding dice
	for e in roll:
		if e == 1 or e == 5 or e == combo:
			continue
		roll.remove(e)

	return roll


	


# Decides whether or not player keeps going, and
# which dice to keep if they are.
def chooseDiceToKeep(roll):

	(combo, x_times) = getCombos(roll)
	while True:

		dice_kept = raw_input("Which dice would you like to keep, enter 0 to stop (e.g. \"1 1 5\" or \"0\"): ")
		dice_kept = dice_kept.split()

		# Didn't enter any dice
		if len(dice_kept) == 0:
			"Please enter at least 1 die to keep."
			continue

		# 0 was part of dice_kept
		if "0" in dice_kept:
			if len(dice_kept) == 1:
				return roll
			print "You included other number along with \"0\"."
			continue

		# Loop through all of the non-point dice and check them
		a = [2, 3, 4, 6]	# All of the non-point numbers
		goodDice = True		# Flag that decides whether dice_kept is okay to return
		for e in a:
			if str(e) in dice_kept:
				if combo == e:
					if dice_kept.count(str(e)) != x_times:
						print "You entered at least one die that isn't worth points."
						goodDice = False
						break
				else:
					print "You entered at least one die that isn't worth points."
					goodDice = False
					break

		if goodDice:
			if dice_kept.count("1") > getOnes(roll):
				print "You don't have that many 1's."
				continue
			if dice_kept.count("5") > getFives(roll):
				print "You don't have that many 5's."
				continue
			return toInt(dice_kept)


def getPoints(roll):
	combo = getComboOrFarklePoints(roll)
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
	return 0, 0


def getComboOrFarklePoints(roll):
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
		if getComboOrFarklePoints(roll) == 1500:
			total += 1
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

# Takes an array of String integers and converts
# them to real integers
def toInt(arr):
	newArr = []
	for e in arr:
		newArr.append(int(e))
	return newArr


# Add the score to the player
def addScore(players, name, totalScore, index, score):
	players[index] = (name, totalScore+score, index)


# Return False if someone has a score higher
# than 10,000
def getWinner(players):
	for e in players:
		if e[1] >= 10000:
			return True
	return False


# After someone has reached 10,000 and each
# player has taken their last turns, find
# the highest score and return that player.
def finalWinner(players):
	highest = players[0]
	for e in players:
		if e[1] > highest[1]:
			highest = e
	return highest


# Instructions for the game
def showInstructions():
	print "Number of Players: 2+"
	print
	print "Object: Acsquire points by rolling the dice"
	print
	print "To Play:"
	print "\tThe first player rolls the 5 dice and either"
	print "\tkeeps their score or can set aside one or"
	print "\tmore dice, then roll again to increase their"
	print "\tscore."
	print
	print "\tIf you score using all 5 dice you can roll again"
	print "\tadding to your first rolls score.  However, you"
	print "\tcan lose all your points if you roll the dice at"
	print "\tany time and the thrown dice do not have a score."
	print
	print "\tEach player takes a turn until one reaches"
	print "\t10,000 points.  Then each player gets one"
	print "\tmore turn to try and beat the winner's score."
	print
	print "Scoring:"
	print "\tEach 1 = 100 points"
	print "\tEach 5 = 50 points"
	print "\t3 1's = 1000 points, x2 for each 1 after 3"
	print "\tThree of a kind of any other number = number on the dice x100, x2 for each one after 3"
	print "\t\tExample: 3 4's = 400, 4 4's = 800, 5 4's = 1600"
	print "\tFarkle (1, 2, 3, 4, 5 OR 2, 3, 4, 5, 6) = 1500"
	print
	print



main()
