#! /usr/bin/env python

def main():
	print
	num = input("How high would you like to find prime numbers? ")

	# List of prime numbers from google
	primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
			31, 37, 41, 43, 47, 53, 59, 61, 67, 
			71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137]

	# List of prime numbers seen so far
	lst = []

	# Index used to loop through list of real primes
	primeIndex = 0

	print
	print "Program Primes -> Googled Primes"
	print

	for i in range(num):
		flag = True
		if (not i % 2 == 0 and not i % 3 == 0) or (i == 2 or i == 3):
			for j in lst:
				if i % j == 0:
					flag = False
			if flag:
				if not i == 1:
					lst.append(i)
				# Use this to compare against numbers in the googled list
				if primeIndex < len(primes):
					print str(i) + " -> " + str(primes[primeIndex])
					primeIndex += 1
				# Otherwise, just print the prime numbers
				else:
					print i


if __name__=='__main__':
	main()



