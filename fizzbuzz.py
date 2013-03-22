#! /usr/bin/env python

# Prints the numbers 1-100 (inclusive).  If the number
# is divisible by 3, it prints "Fizz" instead of the
# number.  If it's divisible by 5, it prints "Buzz".
# If it's divisible by both 3 and 5, it prints "FizzBuzz".

def main():
	for i in range(1,101):
		if i % 3 == 0:
			if i % 5 == 0:
				print "FizzBuzz"
			else:
				print "Fizz"
		elif i % 5 == 0:
			print "Buzz"
		else:
			print i

if __name__=="__main__":
	main()
